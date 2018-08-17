
import time
import serial
from . import daq
import numpy as np

ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

#Turns the laser ON by sending the 'LO' command to the device
def LaserON():
    ser.write("LO" + '\r\n')


#Turns the laser OFF by sending the 'LF' command to the device
def LaserOFF():
    ser.write("LF" + '\r\n')


#This adjusts the wavelength to whatever value is inserted by the user
def AdjustWavelength(value):
    ser.write("WA" + value + '\r\n')


#This adjusts the power to whatever value is inserted by the user
def AdjustPower(value):
    ser.write("LP" + value + '\r\n')



def getArray(begin, end, size):
    start = float(begin)
    finish = float(end)
    stepsize = float(size)
    x = (2*(finish - start)/stepsize) + 2
    return np.zeros((int(x),2), dtype = float)



def SweepWavelength(begin, end, size):
    #This function sweeps the wavelenth from a beginning value to an end value and then back to the beginning value
    #The step size in wavelength is .01nm but digitally it can be controlled down to .001nm
    #It takes whatever the value the wavelenth was and drops it to the value of 'begin' and then begins the sweep

    start = float(begin)
    finish = float(end)
    stepsize = float(size)

    daqArray = getArray(begin,end,size)
    arrayindex = 0
    mystring = "WA" + str(start) + '\r\n'

    #This increases the wavelength by .01 nm until it reaches the value of 'end'
    while start < float(end):
        ser.write(mystring)
        daqArray[arrayindex, 0] = start
        daqArray[arrayindex, 1] = daq.getAverage()
        start  = start + stepsize #This is the step size
        arrayindex = arrayindex + 1
        mystring = "WA" + str(start) + '\r\n'

    #This then sweeps the wavlength back down to 1530nm by a .01 nm step size as well
    #wavelength = 1580.00
    mystring = "WA" + str(finish) + '\r\n'
    while finish > float(begin):
        ser.write(mystring)
        daqArray[arrayindex, 0] = finish
        daqArray[arrayindex, 1] = daq.getAverage()
        arrayindex = arrayindex + 1
        finish  = finish - stepsize #This is the step size
        mystring = "WA" + str(finish) + '\r\n'

    print(daqArray)

def Exit():
    ser.close()
    exit()
