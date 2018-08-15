from tkinter import *
from functions import GUIfunctions as gf



class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Santec TSL210 Laser Control")
        self.pack(fill = BOTH, expand=1)

        LaserON = Button(self, text = "Laser ON", command = gf.LaserON)
        LaserOFF = Button(self, text = "Laser OFF", command = gf.LaserOFF)
        Exit = Button(self, text = "Exit", command = gf.Exit)
        Wavelength = Button(self, text = "Adjust Wavelength", command = lambda: gf.AdjustWavelength(WE.get()))
        Power = Button(self, text = "Adjust Power (mW)", command = lambda: gf.AdjustPower(PE.get()))

        WavelengthEntry = StringVar()
        PowerEntry = StringVar()
        WE = Entry(self, textvariable = WavelengthEntry)
        PE = Entry(self, textvariable = PowerEntry)

        LaserON.place(x=0,y=0)
        LaserOFF.place(x=0,y=25)
        Exit.place(x=0,y=50)
        Wavelength.place(x=30,y=0)
        Power.place(x=30,y=25)
        WE.place(x=60,y=0)
        PE.place(x=60,y=25)

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
