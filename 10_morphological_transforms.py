import numpy as np
import cv2
import config
import matplotlib.pyplot as plt

# pre-defined
FILE_NAME = config.IMG_PATH + "cam1.jpg"
lower_red_1 = np.array([0, 100, 0])
upper_red_1 = np.array([100, 160, 170])
lower_red_2 = np.array([150, 0, 0])
upper_red_2 = np.array([255, 255, 255])

# load image
# img = cv2.imread(FILE_NAME, cv2.IMREAD_COLOR)
cap = cv2.VideoCapture(0)
_, img = cap.read()
cap.release()

# convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask    
mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
mask = cv2.bitwise_or(mask_2, mask_2)
res1 = cv2.bitwise_and(img, img, mask=mask_1)
res2 = cv2.bitwise_and(img, img, mask=mask_2)
res = cv2.bitwise_and(img, img, mask= mask)

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(mask, kernel, iterations=1)
dilation = cv2.dilate(mask, kernel, iterations=2)
morph_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
morph_close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

# masked
erosion_res = cv2.bitwise_and(img, img, mask=erosion)
dilation_res = cv2.bitwise_and(img, img, mask=dilation)
open_res = cv2.bitwise_and(img, img, mask=morph_open)
close_res = cv2.bitwise_and(img, img, mask=morph_close)
gradient_res = cv2.bitwise_and(img, img, mask=gradient)

# show
images = [
  cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(mask_1, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(mask_2, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(erosion, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(dilation, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(morph_open, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(morph_close, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(gradient, cv2.COLOR_GRAY2RGB),

  cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(res1, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(res2, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(res, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(erosion_res, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(dilation_res, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(open_res, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(close_res, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(gradient_res, cv2.COLOR_BGR2RGB),
]
title = [
  "original",
  "mask 1",
  "mask 2",
  "mask",
  "erosion",
  "dilation",
  "open",
  "close",
  "gradient",

  "origin",
  "masked 1",
  "masked 2",
  "marked",
  "erosion marked",
  "dilation marked",
  "open marked",
  "close marked",
  "gradient marked",
]

for i in range(len(images)):
  plt.subplot(2, 9, i+1)
  plt.imshow(images[i])
  plt.title(title[i])
  plt.xticks([])
  plt.yticks([])

plt.show()