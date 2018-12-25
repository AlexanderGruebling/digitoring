import sys
import time
import Adafruit_DHT
import datetime
sensor = Adafruit_DHT.DHT11
pin = 4

h= open("Humidity.txt","w")
t= open("Temperature.txt","w")
while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, pin)
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))
		h.write(str(humidity)+";"+datetime.datetime.now().strftime("%X")+"/"+"\n")
		t.write(str(temperature)+";"+datetime.datetime.now().strftime("%X")+"/"+"\n")		
	else:
    		print('Failed reading. Try again!')
	time.sleep(5)

