##############################
#      IMPORT LIBRARIES      #
##############################

# IMPORT MODULES
import numpy as np
import pandas as pd
import random # to select random images from a folder
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt


# CV2
import cv2

##############################
#                            #
##############################

# DATA AUGMENTATION FUNCTIONS

# HORIZONTAL FLIP
def horizontal_flip(img, flag):
    if flag:
      return cv2.flip(img, 1)
    else:
      return img

# VERTICAL FLIP
def vertical_flip(img, flag):
    if flag:
        return cv2.flip(img, 0)
    else:
        return img

# BRIGHTNESS
def brightness(img, low, high):
  # A RANDOM VALUE HAS BEEN CHOOSE BETWEEN THE LOW AND HIGH VALUES
  value = random.uniform(low, high)
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  hsv = np.array(hsv, dtype = np.float64)
  hsv[:,:,1] = hsv[:,:,1]*value
  hsv[:,:,1][hsv[:,:,1]>255]  = 255
  hsv[:,:,2] = hsv[:,:,2]*value 
  hsv[:,:,2][hsv[:,:,2]>255]  = 255
  hsv = np.array(hsv, dtype = np.uint8)
  img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  return img

# HUE
def hue_image(img, saturation):
  image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  v = image[:, :, 2]
  v = np.where(v <= 255 + saturation, v - saturation, 255)
  image[:, :, 2] = v

  image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

  return image

# FUNCTION TO ADD VALUE LABELS TO THE HISTOGRAM PLOT WITH THE COUNT OF IMAGES
def addlabels(x, y):
  for i in range(len(x)):
    plt.text(i, y[i], y[i], Bbox = dict(facecolor = 'blue', alpha =.8))