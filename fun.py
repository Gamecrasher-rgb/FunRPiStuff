#Measures temperature, humidity, pressure
# BME280 - Adafruit#000000
#Write the data to a file - a time column, temperature, humidity, and pressure
# - Look up Adafruit CircuitPyhton BME280 module
# - update code to use that module

import serial
import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import math
import csv
import numpy as np
import sys
import datetime as dt



i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

temperatures = []
pressures = []
humidities = []
times = []
pm1 = []
pm25 = []
pm10 = []

def average(num):
	
	avg = sum(num)/len(num)
	
	return avg
	
n=1
while n>0:
    temp = bme280.temperature
    temperatures.append(temp)
    average_temp = average(temperatures)
    print('The average temperature is', average_temp)	

#Made a function to calulcate average

#Print Average




