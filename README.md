# paho-mqtt-communication

This repository is showing a basic usage of the paho library in python to enable the communication between 2 clients (both publisher and subscriber).

### What is it doing?

These scripts are synchronizing 2 light traffic controllers with raspberry Pi and using MQTT (M2M communication)

We're using sense_emu package to manipule the Sence Hat Emulator in raspbian (Raspberry Pi OS) so make sure to run this script in a raspbian OS (use a vm).

Each script should be located in a seperate VM and our broker on a another VM.

We're using username/password authentication when connecting to the broker and this needs additional configuration in mosquitto broker. (To disable this just delete the lines setting the credentials in the 2 clients)

### How to execute it?

The client1 should be the first script to run since it is listening and responding to the messages recieved from client1 and make sure that the mosquitto broker is running.