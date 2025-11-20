import cayenne.client  # Cayenne MQTT Client
import RPi.GPIO as GPIO
import time

ledpin = 12  # PWM pin connected to LED
GPIO.setwarnings(False)  # disable warnings
GPIO.setmode(GPIO.BOARD)  # set pin numbering system
GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)  # create PWM instance with frequency
pi_pwm.start(0)  # start PWM of required Duty Cycle 

# MQTT Credentials
MQTT_USERNAME = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # YOUR MQTT USERNAME
MQTT_PASSWORD = "xxxxxxxxxxxxxxx"  # YOUR MQTT PASSWORD
MQTT_CLIENT_ID = "xxxxxxxx"

# The callback for when a message is received from Cayenne.
def on_message(message):
    print("Message received: " + str(message))
    if message.channel == 0:  # Dashboard Slider widget channel. It must be the same.
        try:
            duty_cycle = float(message.value)  # Get the duty cycle from the slider value
            duty_cycle = max(0, min(duty_cycle, 100))  # Ensure duty cycle is between 0 and 100
            pi_pwm.ChangeDutyCycle(duty_cycle)  # Set the PWM duty cycle
            print(f"LED duty cycle set to {duty_cycle}%")
        except ValueError as e:
            print(f"Error converting value to float: {e}")
        except Exception as e:
            print(f"Error in PWM control: {e}")

# Initialize Cayenne MQTT client
client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message  # When a message is received from Cayenne, run on_message function
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

print("Connected to Cayenne. Waiting for commands...")

# Main loop
try:
    while True:
        client.loop()
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
        
except KeyboardInterrupt:
    print("Program stopped by user")
    
finally:
    # Clean up GPIO
    pi_pwm.stop()
    GPIO.cleanup()
    print("GPIO cleaned up and program exited")
