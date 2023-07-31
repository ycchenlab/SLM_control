# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:32:04 2023

@author: ycche
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 1000  # Number of grid points
L = 1  # Grid size
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)


# Super-Gaussian profile parameters
mx = 3  # Super-Gaussian exponent
my = 1
A = 1 # Super-Gaussian amplitude

w0 = L*2  # Super-Gaussian width
dpx = 0
r = 15
# Generate super-Gaussian profile -- it is intensity
target = np.square(A * np.exp(-(np.abs(X-dpx)/(w0/4))**(2*mx)) * np.exp(-(np.abs(Y)/(w0/r))**(2*my)))

fig, ax = plt.subplots()
ax.contour(target, cmap = cm.Blues_r, levels = [0.002, 0.32, 0.62, 0.92, 0.99], linewidths=1)
ax.imshow(target, cmap = cm.Blues)
plt.show()
