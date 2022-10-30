from time import sleep
import paho.mqtt.client as mqtt
from sense_emu import SenseHat
sense = SenseHat()

light = "red"
b=0
g=0
r=255

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("light 2 "+str(msg.payload.decode("utf-8")))
        
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("sofiene", "sofiene")
client.connect("192.168.122.152", 1883, 60)
client.subscribe("light2")
client.loop_start()

sleep(3)

while True :
    if light=="red" :
        client.publish("light1","red")
        light = "green"
        g = 0
        r= 255
        sense.clear((r, g, b))
    else : 
        client.publish("light1","green")
        light = "red"
        r = 0
        g= 255
        sense.clear((r, g, b))
    sleep(3)
