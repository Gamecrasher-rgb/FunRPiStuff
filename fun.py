import os
from tkinter import *   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
import subprocess
import os.path
import ntpath
import shutil
import fnmatch
from typing import Pattern
from tkinter.ttk import *
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

master = Tk()
master.geometry("500x500")

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Current Temoerature")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")

def average(num):
	
	avg = sum(num)/len(num)
	
	return avg
	
n=1
while n>0:
    temp = bme280.temperature
    temperatures.append(temp)
    average_temp = average(temperatures)
    print('The average temperature is', )	

#Made a function to calulcate average

#Print Average




