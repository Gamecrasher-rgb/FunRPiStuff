
import board
from adafruit_bme280 import basic as adafruit_bme280
import numpy as np
from guizero import App, Text

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temperatures = []

def average(num):
	
	avg = sum(num)/len(num)
	
	return avg

app = App(title="Temperaturesd")


while True:
    
    temp = bme280.temperature
    temperatures.append(temp)
    average_temp = average(temperatures)
    welcome_message = Text(app, text=round(average_temp,2))	
    app.display()
#Made a function to calulcate average

#Print Average




