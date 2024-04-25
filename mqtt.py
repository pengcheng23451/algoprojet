import paho.mqtt.client as mqtt
import turtle
import json

# MQTT Broker信息
broker_address = "broker.hivemq.com"
topic = "fpc"

# 创建MQTT客户端
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "fpc")

# 连接到MQTT Broker
client.connect("srv-lora.isep.fr")

# 设置Turtle窗口
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Tableau de Bord Animal")
screen.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.penup() 

#initialisation de couleur
couleur = "red"


# 回调函数，用于处理接收到的MQTT消息
def on_message_callback(client_inst, userdata, message):
    valeur = message.payload.decode("ansi")
    print(message.topic + " " + valeur)

    try:
        nomxylabel = valeur.split(":")
        pen.pendown()
        pen.goto(int(nomxylabel[2]), int(nomxylabel[3]))
        pen.dot(5,couleur)
        pen.penup()
        print("nom :", nomxylabel[1])
        print("position:",nomxylabel[2],nomxylabel[3])

    except Exception as e:
            print(f"Erreur message - {e}")



# 设置MQTT客户端的消息到达回调函数
client.on_message = on_message_callback

# 订阅MQTT主题
client.subscribe("#")

# 开启MQTT客户端的消息循环
client.loop_start()


# 设置Turtle绘图速度
turtle.speed(2)

turtle.mainloop()
