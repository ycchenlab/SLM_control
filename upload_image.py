# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:37:00 2023

@author: ycche
"""
# Import
import detect_heds_module_path 
from holoeye import slmdisplaysdk
import time
import numpy as np
from cv2 import imread, IMREAD_GRAYSCALE
import matplotlib.pyplot as plt
from upload_grating import grating

# Initialize the SLM library
slm = slmdisplaysdk.SLMInstance()

if not slm.requiresVersion(5):
    exit(1)

# Detect SLMs and open a window on the selected SLM
error = slm.open()
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

# Open the SLM preview window in "Fit" mode
from showSLMPreview import showSLMPreview
showSLMPreview(slm, scale=1.0)

# Configure the graph properties
a = 0
b = 0
c = 0

# Reserve memory for the data:
dataWidth = slm.width_px
dataHeight = slm.height_px
print("dataWidth = " + str(dataWidth))
print("dataHeight = " + str(dataHeight))

# The same as:
# data = np.zeros((dataWidth, dataHeight)) 
data = slmdisplaysdk.createFieldSingle(dataWidth, dataHeight)


# Import the DOE
s = 'C:/Users/ycche/git repo/SLM_control/Image/DOE_0825_mGS.png'
S = imread(s, IMREAD_GRAYSCALE)
#S = S/np.max(S)
hy = np.size(S,0)
wx = np.size(S,1)
# ima = np.zeros([1080, 1920])
# ima[int((1080-hy)/2-1):int(1080-(1080-hy)/2-1) , int((1920-wx)/2-1):int(1920-(1920-wx)/2-1)] = S

Nx = wx
Ny = hy
grate = grating(Ny, Nx, px = 50, py = 0, dis_x = 0, dis_y = 0)

# gra = np.zeros([1080, 1920])
# gra[int((1080-Ny)/2-1):int(1080-(1080-Ny)/2-1) , int((1920-Nx)/2-1):int(1920-(1920-Nx)/2-1)] = grate

image = S + grate
image = image/np.max(image)*255
plt.imshow(image)
# Show data on SLM:
error = slm.showData(image)
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

# Wait until the SLM process is closed:
print("Waiting for SDK process to close. Please close the tray icon to continue ...")
error = slm.utilsWaitUntilClosed()
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

# Unloading the SDK 
slm = None

