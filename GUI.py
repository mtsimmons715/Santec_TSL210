#File: GUI.py
#Author: Matthew Simmons
#Last Modified: August 15, 2018
#Purpose: Provide a graphical interface to easily control the Santec TSL210 Laser

from tkinter import *
from functions import GUIfunctions as gf


#The GUI Class

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Santec TSL210 Laser Control")
        self.pack(fill = BOTH, expand=1)

        #Creates the various buttons of the GUI
        LaserON = Button(self, text = "Laser ON", command = gf.LaserON)
        LaserOFF = Button(self, text = "Laser OFF", command = gf.LaserOFF)
        Exit = Button(self, text = "Exit", command = gf.Exit)
        Wavelength = Button(self, text = "Adjust Wavelength", command = lambda: [gf.AdjustWavelength(WE.get()), WE.delete(0,END)])
        Power = Button(self, text = "Adjust Power (mW)", command = lambda: [gf.AdjustPower(PE.get()), PE.delete(0,END)])
        Sweep = Button(self, text = "Sweep Wavelength", command = gf.SweepWavelength)

        #Creates 'Entries' where inputs can be added and interpreted in the form of strings
        #For now we only care to adjust the Power and Wavelength so that is all I made
        WavelengthEntry = StringVar()
        PowerEntry = StringVar()
        WE = Entry(self, textvariable = WavelengthEntry)
        PE = Entry(self, textvariable = PowerEntry)

        #This positions all of the buttons and entries on the GUI
        LaserON.place(x=0,y=0)
        LaserOFF.place(x=0,y=30)
        Exit.place(x=0,y=60)
        Wavelength.place(x=70,y=0)
        Power.place(x=70,y=30)
        WE.place(x=190,y=0)
        PE.place(x=190,y=30)
        Sweep.place(x=40,y=60)


#creates the GUI
root = Tk()
#sets the inital window size of the GUI
root.geometry("400x300")

app = Window(root)

root.mainloop()
