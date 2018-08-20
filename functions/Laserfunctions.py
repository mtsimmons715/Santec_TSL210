from tkinter import *
import time
import serial
#from daqfunctions import daq as dq
import numpy as np

ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

def LaserON():
    mystring = "LO" + '\r\n'
    ser.write(mystring.encode('ascii'))




def LaserOFF():
    mystring = "LF" + '\r\n'
    ser.write(mystring.encode('ascii'))



#This adjusts the wavelength to whatever value is inserted by the user
def AdjustWavelength(value):
    mystring = "WA" + value + '\r\n'
    ser.write(mystring.encode('ascii'))



#This adjusts the power to whatever value is inserted by the user
def AdjustPower(value):
    mystring = "LP" + value + '\r\n'
    ser.write(mystring.encode('ascii'))



#For interfacing with daq, but this project is being abandoned for now
def getArray(begin, end, size):
    start = float(begin)
    finish = float(end)
    stepsize = float(size)
    x = (2*(finish - start + 1)/stepsize)
    return np.zeros((int(x),2), dtype = float)



def SweepWavelength(begin, end, size):
    #This function sweeps the wavelenth from a beginning value to an end value and then back to the beginning value
    #The user chooses the range of wavelengths to sweep as well as the step size
    #Step size can range from .001 - 1
    #It takes whatever the value the wavelenth was and drops it to the value of 'begin' and then begins the sweep

    start = float(begin)
    finish = float(end)
    stepsize = float(size)

    #daqArray = getArray(begin,end,size)
    #arrayindex = 0

    if start < finish:
        mystring = "WA" + str(start) + '\r\n'

        #This increases the wavelength by .01 nm until it reaches the value of 'end'
        while start < float(end) + stepsize:
            ser.write(mystring.encode('ascii'))
            #daqArray[arrayindex, 0] = start
            #daqArray[arrayindex, 1] = daq.getAverage()
            #arrayindex = arrayindex + 1
            start  = start + stepsize #This is the step size
            mystring = "WA" + str(start) + '\r\n'

        #This then sweeps the wavlength back down to 1530nm by a .01 nm step size as well
        #wavelength = 1580.00
        mystring = "WA" + str(finish) + '\r\n'
        while finish > float(begin):
            ser.write(mystring.encode('ascii'))
            #daqArray[arrayindex, 0] = finish
            #daqArray[arrayindex, 1] = daq.getAverage()
            #arrayindex = arrayindex + 1
            finish  = finish - stepsize #This is the step size
            mystring = "WA" + str(finish) + '\r\n'

    elif start > finish:
        mystring = "WA" + str(start) + '\r\n'

        #This increases the wavelength by .01 nm until it reaches the value of 'end'
        while start > float(end) - stepsize:
            ser.write(mystring.encode('ascii'))
            #daqArray[arrayindex, 0] = start
            #daqArray[arrayindex, 1] = 1 #daq.getAverage()
            #arrayindex = arrayindex + 1
            start  = start - stepsize #This is the step size
            mystring = "WA" + str(start) + '\r\n'

        #This then sweeps the wavlength back down to 1530nm by a .01 nm step size as well
        #wavelength = 1580.00
        mystring = "WA" + str(finish) + '\r\n'
        while finish < float(begin):
            ser.write(mystring.encode('ascii'))
            #daqArray[arrayindex, 0] = finish
            #daqArray[arrayindex, 1] = 1 #daq.getAverage()
            #arrayindex = arrayindex + 1
            finish  = finish + stepsize #This is the step size
            mystring = "WA" + str(finish) + '\r\n'

    #print(daqArray)

def Exit():
    ser.close()
    exit()
