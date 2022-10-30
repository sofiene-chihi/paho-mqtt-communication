import paho.mqtt.client as mqtt
from sense_emu import SenseHat
sense = SenseHat()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message = str(msg.payload.decode("utf-8"))
    if message== "red" :
        print("light 1 red")
        client.publish("light2","green")
        b=0
        g=255
        r=0
        sense.clear((r, g, b))

    elif message == "green" :
        print("light 1 green ")
        client.publish("light2","red")
        b=0
        g=0
        r=255
        sense.clear((r, g, b))

client = mqtt.Client()

client.username_pw_set("sofiene", "sofiene")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.122.152", 1883, 60)
client.subscribe("light1")

client.loop_forever()
