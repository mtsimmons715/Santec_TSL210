from tkinter import *
import time
import serial
from . import daq

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

    #All of the rest of the code just gets the response back from the laser and prints it
    #to the terminal to make sure that the command was received correctly
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")



def LaserOFF():
    mystring = "LF" + '\r\n'
    ser.write(mystring.encode('ascii'))

    #All of the rest of the code just gets the response back from the laser and prints it
    #to the terminal to make sure that the command was received correctly
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")


#This adjusts the wavelength to whatever value is inserted by the user
def AdjustWavelength(value):
    mystring = "WA" + value + '\r\n'
    ser.write(mystring.encode('ascii'))

    #All of the rest of the code just gets the response back from the laser and prints it
    #to the terminal to make sure that the command was received correctly
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")


#This adjusts the power to whatever value is inserted by the user
def AdjustPower(value):
    mystring = "LP" + value + '\r\n'
    ser.write(mystring.encode('ascii'))

    #All of the rest of the code just gets the response back from the laser and prints it
    #to the terminal to make sure that the command was received correctly
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")


def daqinfo(begin, end, size):
    print("Hello World!")
    


def getArray(begin, end, size):
    start = float(begin)
    finish = float(end)
    stepsize = float(size)
    x = (2*(finish - start + 1)/stepsize)
    np.zeros((int(x),2))



def SweepWavelength(begin, end, size):
    #This function sweeps the wavelenth from a beginning value to an end value and then back to the beginning value
    #The step size in wavelength is .01nm but digitally it can be controlled down to .001nm
    #It takes whatever the value the wavelenth was and drops it to the value of 'begin'

    start = float(begin)
    finish = float(end)
    stepsize = float(size)

    daqArray = getArray(begin,end,size)
    

    mystring = "WA" + str(start) + '\r\n'

    #This increases the wavelength by .01 nm until it reaches the value of 'end'
    while start < float(end) + stepsize:
        ser.write(mystring.encode('ascii'))
        start  = start + stepsize #This is the step size
        mystring = "WA" + str(start) + '\r\n'

    #This then sweeps the wavlength back down to 1530nm by a .01 nm step size as well
    #wavelength = 1580.00
    mystring = "WA" + str(finish) + '\r\n'
    while finish > float(begin):
        ser.write(mystring.encode('ascii'))
        finish  = finish - stepsize #This is the step size
        mystring = "WA" + str(finish) + '\r\n'



def Exit():
    ser.close()
    exit()
