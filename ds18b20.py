import cayenne.client #Cayenne MQTT Client
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
import time

MQTT_USERNAME  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"#YOUR MQTT USERNAME
MQTT_PASSWORD  = "xxxxxxxxxxxxxxxxx"#YOUR MQTT PASSWORD
MQTT_CLIENT_ID = "xxxxxxxxxxx"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
  client.loop()
  temp_c = sensor.get_temperature()
  temp_c = str(round(temp_c))
  temp_f = (float(temp_c)*1.8+32)
  temp_k = (float(temp_c)+ 273.15)
  print("The temperature_C %s C" % temp_c)
  print("The temperature_F %s F" % temp_f)
  print("The temperature_K %s K" % temp_k)
  print("---------------TEMPERATURE_DS18B20---------------")

  value1 = temp_c
  client.celsiusWrite(5, value1)
  value2 = temp_f                        
  client.fahrenheitWrite(6, value2)  
  value3 = temp_k                        
  client.kelvinWrite(7, value3)                     
  time.sleep(1)
