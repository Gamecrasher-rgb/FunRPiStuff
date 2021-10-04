
import board
#from adafruit_bme280 import basic as adafruit_bme280
import numpy as np
from guizero import App, Text
import numpy as np

#i2c = board.I2C()
#bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temperatures = []

def average(num):
	
	avg = sum(num)/len(num)
	
	return avg

app = App(title="Temperatures")


while True:
    temp = np.random.rand(20,30)
    temperatures.append(temp)
    average_temp = average(temperatures)
    welcome_message = Text(app, text=np.round(average_temp,2))
    app.display()



