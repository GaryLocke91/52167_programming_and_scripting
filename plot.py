#This program displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4]

import numpy as np
import matplotlib.pyplot as plt

#Returns an array of evenly spaced values within the interval 0.0-4.5 in steps of 0.5
x = np.arange(0.0, 4.5, 0.5)

#Stores each set of values to plot as variables
y1 = x
y2 = x**2
y3 = x**3

#Plots the x and y values as lines
plt.plot(y1, y1, label="f(x)")
plt.plot(y1, y2, label="g(x)")
plt.plot(y1, y3, label="h(x)")

#Creates a legend, title, axis labels, and a grid
plt.legend()
plt.title("f(x)=x, g(x)=x^2 and h(x)=x^3")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.grid(which='major', axis='both')

plt.show()