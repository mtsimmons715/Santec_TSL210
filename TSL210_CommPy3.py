#File: TSL210_CommPy3.py
#Author: Matthew Simmons
#Last Modified: August 15, 2018
#Purpose: Continuously running loop that lets the user input any commands from the manual to the laser
#         rather than a limited few if using the GUI 


import time
import serial


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print ('Enter your commands below. Insert "exit" to leave the application.')

#input=1
while 1 :
    # get keyboard input
    command = input(">> ")

    #If 'exit' is typed by the user, then it ends the connection and closes the program
    if command == 'exit':
        ser.close()
        exit()
    else:
        # Send the character to the device
        # Note that '\r\n' is appended to the end of the write statement
        # This is because the delimiter setting on the laser is currently CR/LF
        # This requires that '\r\n' be appended to the end of every write statement that is sent to the laser
        # in order to be interpreted correctly by the laser
        # Delimiter settings can be changed to CR or LF or CR/LF. CR - '\r' LF - '\n' CR/LF - '\r\n'
        # How to change this setting can be found in the User Manual under section 9-2
        mystring = command + '\r\n'
        ser.write(mystring.encode('ascii'))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1).decode('ascii')

        if out != '':
            print (">>" + out)
        else:
            print ("No Output")
