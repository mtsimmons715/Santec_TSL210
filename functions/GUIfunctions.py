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
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")



def AdjustWavelength(value):
    mystring = "WA" + value + '\r\n'
    ser.write(mystring.encode('ascii'))
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")



def AdjustPower(value):
    mystring = "LP" + value + '\r\n'
    ser.write(mystring.encode('ascii'))
    out = ''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode('ascii')

    if out != '':
        print (">>" + out)
    else:
        print ("No Output")



def SweepWavelength():
    #Still figuring this one out
    wavelength = 1530.00
    mystring = "WA" + str(wavelength) + '\r\n'
    while wavelength < 1580.00:
        ser.write(mystring.encode('ascii'))
        wavelength  = wavelength + .01
        mystring = "WA" + str(wavelength) + '\r\n'
    wavelength = 1580.00
    mystring = "WA" + str(wavelength) + '\r\n'
    while wavelength > 1530.00:
        ser.write(mystring.encode('ascii'))
        wavelength  = wavelength - .01
        mystring = "WA" + str(wavelength) + '\r\n'



def Exit():
    ser.close()
    exit()
