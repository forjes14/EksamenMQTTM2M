import paho.mqtt.client as mqtt
import json
import requests


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("data/outParticle")


def on_message(client, userdata, msg):
    try:
        message = json.loads(str(msg.payload)[2:len(str(msg.payload))-1])
        print_message(message)
    except ValueError:
        print("Message not in JSON format.")


def print_message(message):
    print("location : " + message["location"])
    print("temp : " + message["temp"])
    print("humidity : " + message["humidity"])
    print("movement : " + message["movement"])
    print("photoVal : " + message["photoVal"])
    print("ppm : " + message["ppm"])
    print("")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username="", password="")
    client.connect(host="", port=)
    client.loop_forever()


main()
