
import board
#from adafruit_bme280 import basic as adafruit_bme280
import numpy as np
from guizero import *
import numpy as np

#i2c = board.I2C()
#bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temperatures = []

def average(num):
	
	avg = sum(num)/len(num)
	
	return avg

app = App(title="Temperature")

def do_nothing():
    temp = np.random.random(20,30)
    temperatures.append(temp)
    averagetemp = average(temperatures)
    text = Text(app,text = str(averagetemp))
button = PushButton(app, command=do_nothing)
app.display()




