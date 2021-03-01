import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import psutil

mqttBroker ="localhost"

client = mqtt.Client("Temperature_Inside", protocol=mqtt.MQTTv311)
client.connect(mqttBroker, port=1883)

while True:
    cpu_usage = str(psutil.cpu_percent())
    msg = '{"cpu_usage": '+cpu_usage+'}'
    client.publish("cpu_info", msg)
    print(msg)
    time.sleep(1)
