# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:51:15 2023

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt


def grating(Ny, Nx, px, py, dis_x, dis_y):
    # The pixel number per grating
    Nx = Nx
    Ny = Ny
    px = px
    py = py
    
    # displacement shift on axis
    dis_x = dis_x
    dis_y = dis_y
    
    # create image
    imagex = np.zeros([Ny, Nx])
    imagey = np.zeros([Ny, Nx])
    
    # The blaze grating number per grating
    if px != 0:
        nx = Nx // px
    else:
        nx = Nx
        
    if py != 0:
        ny = Ny // py
    else:
        ny = Ny
        
    # y direction grating
    for j in range(Nx):
        for i in range(ny):
            if py == 0:
                break
            s = np.linspace(0, 255, num = py)
            imagey[py*i + dis_x : py*(i+1) + dis_y, j] = s
    
    # x direction grating
    for j in range(Ny):
        for i in range(nx):
            if px == 0:
                break
            s = np.linspace(0, 255, num = px)
            imagex[j, px*i + dis_x : px*(i+1) + dis_x] = np.transpose(s)
    
    image = imagex+imagey
    image = image/np.max(image)*255
    return image