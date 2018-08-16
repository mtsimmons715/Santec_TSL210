from tkinter import *
import time
import serial

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


#This adjusts the wavelength to whatever the value inserted by the user is
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


#This adjusts the power to whatever the value inserted by the user is
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


#I want to change this so that you can put the range of the sweep that is desired
#I'll do that soon
def SweepWavelength():
    #This function sweeps the wavelenth from 1530nm to 1580nm with a step size of .01nm
    #It takes whatever the value the wavelenth was and drops it to 1530nm
    wavelength = 1530.00
    mystring = "WA" + str(wavelength) + '\r\n'

    #This increases the wavelength by .01 nm until it reaches 1580nm
    while wavelength < 1580.00:
        ser.write(mystring.encode('ascii'))
        wavelength  = wavelength + .01
        mystring = "WA" + str(wavelength) + '\r\n'

    #This then sweeps the wavlength back down to 1530nm by a .01 nm step size as well
    wavelength = 1580.00
    mystring = "WA" + str(wavelength) + '\r\n'
    while wavelength > 1530.00:
        ser.write(mystring.encode('ascii'))
        wavelength  = wavelength - .01
        mystring = "WA" + str(wavelength) + '\r\n'



def Exit():
    ser.close()
    exit()
