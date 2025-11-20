import cayenne.client #zafron(Cayenne) MQTT Client
import RPi.GPIO as GPIO
import cayenne.client

GPIO.setmode(GPIO.BCM)
dataPin  = 24  # Pin for Data (GPIO 24)
latchPin = 23  # Pin for Latch (GPIO 23)
clockPin = 18  # Pin for Clock (GPIO 18)

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)

# Variables
shift_data = 0b00000000  # Initial state of the shift register (all LEDs off)
previous_shift_data = 0b00000000

# Function to update shift register
def update_shift_register():
    global shift_data, previous_shift_data
    if shift_data != previous_shift_data:
        previous_shift_data = shift_data
        GPIO.output(latchPin, GPIO.LOW)
        shift_out(shift_data)
        GPIO.output(latchPin, GPIO.HIGH)

# Shift out data (similar to Arduino's shiftOut function)
def shift_out(data):
    for i in range(8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (data >> (7 - i)) & 0x01)
        GPIO.output(clockPin, GPIO.HIGH)

MQTT_USERNAME  = "60cb2573-19c4-4769-9985-faf6e125da01"#YOUR MQTT USERNAME
MQTT_PASSWORD  = "00000000C3E91A06"#YOUR MQTT PASSWORD
MQTT_CLIENT_ID = "753D49C6"

def on_message(message):
    global shift_data  # Add this line to declare shift_data as global
    print("message received: " + str(message))
    if message.channel==1: 
        if message.value=="1": 
          shift_data |= 0b00000001
        elif message.value=="0": 
          shift_data &= 0b11111110
            
    if message.channel==2: 
        if message.value=="1": 
          shift_data |= 0b00000010
        elif message.value=="0": 
          shift_data &= 0b11111101
            
    if message.channel==3: 
        if message.value=="1": 
          shift_data |= 0b00000100
        elif message.value=="0": 
          shift_data &= 0b11111011
            
    if message.channel==4: 
        if message.value=="1": 
          shift_data |= 0b00001000 
        elif message.value=="0": 
          shift_data &= 0b11110111 

    if message.channel==5: 
        if message.value=="1": 
          shift_data |= 0b00010000
        elif message.value=="0": 
          shift_data &= 0b11101111  
            
    if message.channel==6: 
        if message.value=="1": 
          shift_data |= 0b00100000 
        elif message.value=="0": 
          shift_data &= 0b11011111  
            
    if message.channel==7: 
        if message.value=="1": 
          shift_data |= 0b01000000 
        elif message.value=="0": 
          shift_data &= 0b10111111  
            
    if message.channel==8: 
        if message.value=="1": 
          shift_data |= 0b10000000 
        elif message.value=="0": 
          shift_data &= 0b01111111  
    update_shift_register()

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
  client.loop()
