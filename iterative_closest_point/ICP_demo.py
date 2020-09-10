# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:32:39 2020

@author: Muhammad Fazlur Rahman
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos
from mpl_toolkits import mplot3d

def f(X, Y):
    return np.sin(X)*np.cos(Y)

#Create initial point clouds
m = 80
n = m^2

maxVal = 2
minVal = -2
        
x = np.linspace(minVal, maxVal, m)
y = np.linspace(minVal, maxVal, m)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Plot data
fig = plt.figure("ICP")
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, color="G", edgecolor='none')
ax.set_title('Z = sin(X) * cos(Y)');
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z');

