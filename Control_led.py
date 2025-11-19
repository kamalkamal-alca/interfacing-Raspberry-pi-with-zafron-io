import cayenne.client #Cayenne MQTT Client
import RPi.GPIO as GPIO
import cayenne.client

led1 = 15 
led2 = 15
led3 = 18 
led4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

MQTT_USERNAME  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"#YOUR MQTT USERNAME
MQTT_PASSWORD  = "xxxxxxxxxxxxxxxxxxx"#YOUR MQTT PASSWORD
MQTT_CLIENT_ID = "xxxxxxxxxxxxx"

def on_message(message):
    print("message received: " + str(message))
    if message.channel==1: 
        if message.value=="1": 
          GPIO.output(led1, GPIO.HIGH)
        elif message.value=="0": 
            GPIO.output(led1, GPIO.LOW)
            
    if message.channel==2: 
        if message.value=="1": 
          GPIO.output(led2, GPIO.HIGH)
        elif message.value=="0": 
            GPIO.output(led2, GPIO.LOW)
            
    if message.channel==3: 
        if message.value=="1": 
          GPIO.output(led3, GPIO.HIGH)
        elif message.value=="0": 
            GPIO.output(led3, GPIO.LOW)
            
    if message.channel==4: 
        if message.value=="1": 
          GPIO.output(led4, GPIO.HIGH)
        elif message.value=="0": 
            GPIO.output(led4, GPIO.LOW)
            

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
  client.loop()
