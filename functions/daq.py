#import ctypes as ct
import numpy as np
import nidaqmx
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import sys

#maximize imports
from scipy.optimize import minimize
# Imports for plotting path
#import matplotlib as mpl
#3.2mw/1.42v
#2.2535 mw/v

# A list for storing lists of our optimization path and values.
path = []
# uncomment the two below lines if you want to use the runChart function

# Function: surface_plot
# Purpose: Given a matrix, convert it into a form that matplotlib knows how
# to plot in 3d space as a surface.
# Parameters: the matrix to be plotted (formatted as an x by z matrix, whose
# values are the values of the surface at that point).
# Returns: a tuple containing the figure, axis, and surface.
# Surface plot code courtesy of CMCDragonkai, see
# https://gist.github.com/CMCDragonkai/dd420c0800cba33142505eff5a7d2589
def surface_plot (matrix, **kwargs):
    # acquire the cartesian coordinate matrices from the matrix
    # x is cols, y is rows
    (x, y) = np.meshgrid(np.arange(matrix.shape[0]), np.arange(matrix.shape[1]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, matrix, **kwargs)
    return (fig, ax, surf)

# Function: animate
# Purpose: Produce a plot that has the same function as an oscilloscope screen.
# Parameters: Auto handled by the matplotlib FuncAnimation function.
# Returns: None
def animate(i):
    # Get x and y data.
    x = np.array(np.linspace(0,100,100))
    y = np.array(get100data()) * 1000
    # Get the average value
    avg = np.mean(y)
    z = np.full((100,1), avg)
    # Clear the figure, and plot the new data
    ax1.cla()
    # The plot:
    lim = avg * 1.5
    plt.axis([0,100,0,lim])
    ax1.plot(x,y,'r-',x,z,'b-')
    plt.ylabel('Voltage (mv)')
    plt.xlabel('Measurement #')
    plt.title("DAQ Real-Time Measurements")
    plt.legend(['Measured voltage','Average = ' + str('{:.2f}'.format(avg)) + ' mV'], loc='upper left', bbox_to_anchor=(0.6,1))

# Function: get100data
# Purpose: Reads 100 samples from cDAQ1Mod1/ai0 at 10kHz sample rate. Stores
# the results in an array.
# Parameters: None
# Returns: The array of 100 sample values.
def get100data():
    with nidaqmx.Task() as task:
        # Configure task
        task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
        task.timing.cfg_samp_clk_timing(10000, samps_per_chan = 100)
        # Read the data
        data = task.read(number_of_samples_per_channel=100)
        return data

# Function: getAverage
# Purpose: Return the average value of 100 samples read from the DAQ. Automatically
# calls get100data().
# Parameters: None
# Returns: A value, the average of 100 samples.
def getAverage():
    a = np.array(get100data())
    avg = np.mean(a) * 1000
    return avg

# THIS FUNCTION IS NOT YET COMPLETE
# Function: calcPercent
# Purpose:
# Parameters:
# Returns:
def calcPercent():
    avg = getAverage()
    percent = 2.2535*avg/3.2
    return percent

# Function: runChart
# Purpose: Run the o-scope chart directly from the daq script; no need to
# open sampleGUI.
# Parameters: None
# Returns: None; opens a new window displaying a real-time updating chart.
def runChart():
    ani = animation.FuncAnimation(fig, animate, interval=20)
    plt.show()



# Function: getPath
# Purpose: return the array stored within daq that is called "path". It is an
# array of arrays; each entry represents another n-dimension reading
# (currently x,y,voltage).
# Parameters: None
# Returns: An array of arrays containing, sequentially, the path taken during
# the optimzation process.
def getPath():
    return path


# Function: get100data
# Purpose: Reads 100 samples from cDAQ1Mod1/ai0 at 10kHz sample rate. Stores
# the results in an array.
# Parameters: None
# Returns: The array of 100 sample values.
def getTimedData(samplerate, sampletime):
    with nidaqmx.Task() as task:
        # Configure task
        task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
        task.timing.cfg_samp_clk_timing(samplerate, samps_per_chan = samplerate * sampletime)
        # Read the data
        data = task.read(number_of_samples_per_channel=samplerate * sampletime)
        mean = np.mean(data)
        return mean



def showHelp():
    print("----------DAQ Program Help----------")
    print("This program has the following functions, taken as command line arguments:")
    print(" - intensity (creates a surface plot showing the voltage after scanning the surface)")
    print(" - voltage (instantaneous voltage measurement)")
    print(" - maximize (moves the stage to the location of highest voltage)")
    print(" - scope (opens a simple digital oscilloscope)")
    

def whichpiezo():
    try:
        args = sys.argv[2]
        if args == "s": return "secondary"
        else: return "primary"
    except IndexError:
        which = raw_input("Primary or secondary controller? Type 'p' or 's': ")
        if which == "s": return "secondary"
        else: return "primary"




if __name__ == "__main__":
    try:
        kargs = sys.argv[1]
        if kargs == "help":
            showHelp()
        elif kargs == "intensity":
            xzIntensity(whichpiezo())
        elif kargs == "voltage":
            print (getTimedData(8000, 1))
        elif kargs == "maximize":
            maximize(whichpiezo())
        elif kargs == "scope":
            fig = plt.figure()
            ax1 = fig.add_subplot(1,1,1)
            ani = animation.FuncAnimation(fig, animate, interval=20)
            plt.show()
            runChart()
        else:
            print(sys.argv[1] + " is not a valid command. The following are legal commands: \n")
            showHelp()
    except IndexError:
        showHelp()
    #values = np.zeros((2000,2000))
    #print values
