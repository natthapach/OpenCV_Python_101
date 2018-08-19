import numpy as np
import cv2
import config
import matplotlib.pyplot as plt

# pre-defined
FILE_NAME = config.IMG_PATH + "cam1.jpg"
lower_red = np.array([20, 120, 0])
upper_red = np.array([255, 160, 190])

# load image
# img = cv2.imread(FILE_NAME, cv2.IMREAD_COLOR)
cap = cv2.VideoCapture(0)
_, img = cap.read()
cap.release()

# convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask= mask)

# blur
kernel = np.ones((15, 15), np.float32)/500
smoothed = cv2.filter2D(res, -1, kernel)

gaussian = cv2.GaussianBlur(res, (15, 15), 0)

median = cv2.medianBlur(res, 15)

bilateral = cv2.bilateralFilter(res, 15, 75, 75)



# show
images = [
  img,
  res,
  smoothed,
  gaussian,
  median,
  bilateral,
]
title = [
  "original",
  "masked",
  "smoothed",
  "gaussian",
  "median",
  "bilateral",
]

for i in range(len(images)):
  plt.subplot(2, 3, i+1)
  plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
  plt.title(title[i])
  plt.xticks([])
  plt.yticks([])

plt.show()