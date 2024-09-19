# Written by Inuka Amaratunga (inuka.amaratunga@gmail.com)

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Frames in final animation
max_steps = 120
# grid_w is the wingspan of the grid
# that is to say, the grid is 2*grid_w wide and tall
grid_w = math.pi
# view_w is the wingspan of the viewport 
view_w = 15
# Amount of gridlines to draw
amt = 10
# Change the caption on the output
transform_caption = "Transform $e^{z}$"
# The transformation
def transform(z):
    return np.exp(z)

save_to_file = False
file_output = "./output_complex.gif"


#
# WARNING:
# Everything below here is probably useless for most people. You can do lots of things wiht just the above settings.
#

# Amount of points to draw in each line
pw = 1000
# Minimum and maximum coordinates
minp = (-grid_w, -grid_w)
maxp = (grid_w, grid_w)
# Minimum and maximum coordinates
viewmin = (-view_w, -view_w)
viewmax = (view_w, view_w)
# frames per second
fps = 60
# Interval between major lines
major_interval = 1
# Choose whether to colour major lines or not
major_lines = False
# Colour of y lines
col1 = (1,0,0)
# Colour of x lines
col2 = (0,0,1)
# Colour of major lines
majcol = (1, 0, 0)

fig, ax = plt.subplots()

# Starting grid 
arr = []
# Grid after transformation
arrp = []

# We can't pass into functions such as animate, so we choose to keep these in global scope
# Perhaps there's a nicer way to do this, but this werks
# Gridlines before transformation
# These are added to by the plot_complex function which unpack and populate these lists
# If polar is enabled, we populate x with the modulus and y with the angle
arr_x = []
arr_y = []
# After transformation
arrp_x = []
arrp_y = []
# List of colors 
cols = []

def animate(frame):
    prog = frame/(max_steps-1)
    t=prog
    
    ax.cla()
    plt.xlim((viewmin[0], viewmax[0]))
    plt.ylim((viewmin[1], viewmax[1]))
    ax.set_aspect('equal', adjustable='box')

    for (x, y, xp, yp, col) in zip(arr_x, arr_y, arrp_x, arrp_y, cols):
        ax.plot(interp(x, xp, t), interp(y, yp, t), color=col, alpha=1, linewidth=1)
    
    ax.scatter([0],[0],marker="o", color="red")

    plt.xlabel('$\Re(z)$', fontsize=18)
    plt.ylabel('$\Im(z)$', fontsize=16)
    fig.suptitle(transform_caption)
    ax.set_title(f"t = {round(prog,4)}")
    print(prog)

def plot_complex(arr, arrp, steps=max_steps):
    global arr_x
    global arr_y
    global arrp_x
    global arrp_y

    arr_x = [x.real for (x) in arr]
    arr_y = [x.imag for (x) in arr]
    
    arrp_x = [x.real for (x) in arrp]
    arrp_y = [x.imag for (x) in arrp]

    arr_x = np.array(arr_x)
    arr_y = np.array(arr_y)
    arrp_x = np.array(arrp_x)
    arrp_y = np.array(arrp_y)


def interp(l1, l2, t):
    return (l1 * (1-t) + l2 * t)/2

def main():
    arr = []

    print(f"Constructing input array:")

    # Generate equally spaced vertical lines
    count = 0
    for x in np.linspace(minp[0], maxp[0], num=amt):
        subarray = []
        for y in np.linspace(minp[1], maxp[1], num=int(pw)):
            subarray.append(x + y * 1j)
        arr.append(subarray)
        if (major_lines and major_count % major_interval == 0):
            cols.append(majcol)
        else:
            cols.append(col1)

        count += 1


    # Generate equally spaced horizontal lines
    count = 0
    for y in np.linspace(minp[1], maxp[1], num=amt):
        subarray = []
        for x in np.linspace(minp[0], maxp[0], num=int(pw)):
            subarray.append(x + y * 1j)
        arr.append(subarray)
        if (major_lines and count % major_interval == 0):
            cols.append(majcol)
        else:
            cols.append(col2)

        count += 1
    
    print(f"Transforming")
    arr = np.array(arr)
    arrp = transform(np.array(arr))
    
    print(f"Plotting transformation")
    plot_complex(arr, arrp)
    
    ani = FuncAnimation(fig = fig, func = animate, interval = 1/fps, frames = max_steps, repeat=False)
    # Use only one of the following at a time: plt.show() for live preview and save to save to file
    if save_to_file:
        ani.save(filename=file_output, writer="ffmpeg")
    else:
        plt.show()



main()




