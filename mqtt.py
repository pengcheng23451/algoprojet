import paho.mqtt.client as mqtt
import turtle
import json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "fpc")
client.connect("srv-lora.isep.fr")


screen = turtle.Screen()
screen.setup(500, 500)
screen.title("Tableau de Bord Animal")
screen.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.penup()



def on_message_callback(client_inst, userdata, message):
    try:
        valeur = message.payload.decode("ansi")
        print(message.topic + " " + valeur)
        valeur_json = json.loads(valeur)
        valeur_lora = valeur_json["object"]["message"]
        liste_recu = valeur_lora.split(":")
        position = (int(liste_recu[1]), int(liste_recu[2]))
        nom_animal = liste_recu[0]
        dessiner_point(position)
        print("Nom:", nom_animal)
        print("Position:", position)
    except Exception as e:
        print("Erreur du message:", e)



def dessiner_point(position, couleur="black"):
    pen.pendown()
    pen.goto(position)
    pen.dot(5, couleur)
    pen.penup()

client.on_message = on_message_callback

client.subscribe("#")
client.loop_start()

turtle.mainloop()