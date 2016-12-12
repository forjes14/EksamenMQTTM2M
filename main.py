import paho.mqtt.client as mqtt
import google.cloud.pubsub as pubsub

message = ""

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("data/outParticle")


def on_message(client, userdata, msg):
    messageRaw = str(msg.payload)
    message = messageRaw[2:len(messageRaw)-1]
    publish_message(message)


def publish_message(message):
    pubsub_client = pubsub.Client()
    topic_name = 'sensor-data-m2m'
    topic = pubsub_client.topic(topic_name)
    topic.create()
    topic.publish(message)
    print("Printed to pub/sub topic "+ topic_name)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username="123", password="123")
    client.connect(host="m21.cloudmqtt.com", port=11583)
    client.loop_forever()


main()
