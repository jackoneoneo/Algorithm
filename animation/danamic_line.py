'''
动态 Sin函数图
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=False)


def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 200)
    return ln,


def update(frame):
    # y = 2 * frame
    xdata.append(frame)
    ydata.append(2 * frame)
    ln.set_data(xdata, ydata)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 100, 128),
                    init_func=init, blit=True)
plt.show()
