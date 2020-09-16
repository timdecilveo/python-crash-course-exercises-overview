import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Matplotlib Exercises
# Exercises
# Follow the instructions to recreate the plots using this data:


x = np.arange(0,100)
y = x*2
z = x**2
print(f"x:")
print(f"{x}")
print(f"y:")
print(f"{y}")
print(f"z:")
print(f"{z}")
print("-----------------------------------------------")
# Exercise 1
# ** Create a figure object called fig using plt.figure() **
fig = plt.figure()
# ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**
ax.plot(x, y)
ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2.
# Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**
fig_2 = plt.figure()
fig_2_ax_one = fig_2.add_axes([0.1, 0.1, 0.8, 0.8])
fig_2_ax_two = fig_2.add_axes([0.2,0.5,0.2,0.2])

# ** Now plot (x,y) on both axes. And call your figure object to show it.**
fig_2_ax_one.plot(x, y, color='purple')
fig_2_ax_one.set_title('title')
fig_2_ax_one.set_xlabel('x')
fig_2_ax_one.set_ylabel('y')

fig_2_ax_two.plot(x, y, color='red')
fig_2_ax_two.set_title('title2')
fig_2_ax_two.set_xlabel('x2')
fig_2_ax_two.set_ylabel('y2')

# Exercise 3
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**
fig_3 = plt.figure()
fig_3_ax_one = fig_3.add_axes([0.09,0.09,1,1])
fig_3_ax_two = fig_3.add_axes([0.2,0.5,0.4,0.4])
# ** Now use x,y, and z arrays to recreate the plot below.
# Notice the xlimits and y limits on the inserted plot:**
fig_3_ax_one.plot(x, z, color='blue')
fig_3_ax_one.set_title('---')
fig_3_ax_one.set_xlabel('x')
fig_3_ax_one.set_ylabel('z')

fig_3_ax_two.plot(x, y, color='blue')
fig_3_ax_two.set_title('zoom')
fig_3_ax_two.set_xlabel('x')
fig_3_ax_two.set_ylabel('y')
fig_3_ax_two.set_xlim(20, 22)
fig_3_ax_two.set_ylim(30, 50)

# Exercise 4
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**
fig_4, fig_4_ax_one = plt.subplots(nrows=1, ncols=2)
# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**
fig_4_ax_one[0].plot(x, y, color='blue', ls='--')
fig_4_ax_one[0].set_title('1st Ax')
fig_4_ax_one[0].set_xlabel('X')
fig_4_ax_one[0].set_ylabel('Y')

fig_4_ax_one[1].plot(x, z, color='red')
fig_4_ax_one[1].set_title('2nd Ax')
fig_4_ax_one[1].set_xlabel('X')
fig_4_ax_one[1].set_ylabel('Y')
# ** See if you can resize the plot by adding the figsize() argument in plt.subplots()
# are copying and pasting your previous code.**


plt.tight_layout()
plt.show()
# Great Job!