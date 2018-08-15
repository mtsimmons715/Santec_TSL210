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
    print("Hello")



def AdjustPower(value):
    print("Hi")



def SweepWavelength():
    print("Hello")

def Exit():
    exit()
