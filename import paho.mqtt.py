import paho.mqtt.client as mqtt
import time
import random
import json


def genere_msg(id):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    temp = random.randint(36,39)
    return f"name: {id},position: ({x},{y}),temperature: {temp}"


def ajoute_json(msg):
    msg_dico = {"simulation":{"message":msg}}
    return json.dumps(msg_dico)

def publie_msg(msg_json):
    print(f"Publie : \"{msg_json}\"...")
    client.publish("emulateur_colliers", msg_json)

# Programme principal

colliers = ["Marguerite", "Medor", "Felix"]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "fpc")
client.connect("srv-lora.isep.fr")
#client.connect("broker.hivemq.com")

while True:
    for collier in colliers:
        msg = genere_msg(collier)
        msg_json = ajoute_json(msg)
        publie_msg(msg_json)
        time.sleep(3)