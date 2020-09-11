# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:32:39 2020

@author: Muhammad Fazlur Rahman
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib
from math import sin, cos
from mpl_toolkits import mplot3d

def f(X, Y):
    return np.sin(X)*np.cos(Y)

#Create initial point clouds
m = 80
n = m*m

maxVal = 2
minVal = -2
        
x = np.linspace(minVal, maxVal, m)
y = np.linspace(minVal, maxVal, m)

X_plot, Y_plot = np.meshgrid(x, y)
Z_plot = f(X_plot, Y_plot)

X = X_plot.reshape(1, 6400)
Y = Y_plot.reshape(1, 6400)
Z = f(X, Y)

D = np.vstack([X, Y, Z])
# Plot data
fig = plt.figure("ICP")
ax = plt.axes(projection='3d')
ax.plot_surface(X_plot, Y_plot, Z_plot, rstride=5, cstride=5, color="G", edgecolor='none')
ax.set_title('Z = sin(X) * cos(Y)');
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z');

# Create New Cloud Points, Translated and Rotated from The Original

# Translation values (a.u.):
Tx = 0.5;
Ty = -0.3;
Tz = 0.2;

# Translation vector
T = np.array([[Tx], [Ty], [Tz]]);

# Rotation values (rad.):
rx = 0.3;
ry = -0.2;
rz = 0.05;

Rx = np.array([[1, 0, 0],
               [0, cos(rx), -sin(rx)],
               [0, sin(rx), cos(rx)]])
  
Ry = np.array([[cos(ry), 0, sin(ry)],
               [0, 1, 0],
               [-sin(ry), 0, cos(ry)]])
  
Rz = np.array([[cos(rz), -sin(rz), 0],
               [sin(rz), cos(rz), 0],
               [0, 0, 1]])
    
R = np.matmul(np.matmul(Rx, Ry), Rz)

M = np.add(np.matmul(R, D), np.matlib.repmat(T, 1, n))
MX_plot = M[0][:].reshape(80, 80)
MY_plot = M[1][:].reshape(80, 80)
MZ_plot = f(MX_plot, MY_plot)

ax.plot_surface(MX_plot, MY_plot, MZ_plot, rstride=5, cstride=5, color="R", edgecolor='none')