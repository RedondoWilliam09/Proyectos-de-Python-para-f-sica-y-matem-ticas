import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 60))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=True, save_count=500)

# To save the animation, use e.g.
#
ani.save("movie.gif")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.gif", writer=writer)

plt.show()