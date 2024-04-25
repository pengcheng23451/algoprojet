import paho.mqtt.client as mqtt
import turtle

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "fpc")
# client.connect("srv-lora.isep.fr")
client.connect("broker.hivemq.com")

def on_message_callback(client_inst, userdata, message):
  valeur = message.payload.decode("ansi")
  print(message.topic + " " + valeur)

  if valeur == "fin":
    turtle.bye()
    exit()




  elif valeur[0] == "p":
    try:
      parts = valeur.split(":")
      # 确保消息有足够的部分：'动物名', 'x', 'y', 't'
      if len(parts) < 5: # 注意，现在期望至少有5部分，包括 'p'
        print("Error: Missing information in the message.")
        return
      
      animal_name = parts[1] # 动物名
      x, y, t = int(parts[2]), int(parts[3]), int(parts[4]) # 位置和温度
      turtle.goto(x, y) # 移动到指定位置
      # 在图形界面显示温度
      turtle.write(f" {animal_name}: Temp: {t}°C", move=False, align="left", font=("Arial", 10, "normal"))
      turtle.penup()
      turtle.forward(20)
    except ValueError as e:
      print(f"Error in position or temperature - {e}")
    except Exception as e:
      print(f"Unexpected error - {e}")



      
  elif valeur[0] == "c":
    try:
      couleur = valeur.split(":")[1]
      turtle.color(couleur)
    except Exception as e:
      print(f"Erreur de couleur - {e}")
  else:
      print("Erreur : commande inconnue...")

client.on_message = on_message_callback
client.subscribe("Panda")
client.loop_start()

turtle.mainloop()
