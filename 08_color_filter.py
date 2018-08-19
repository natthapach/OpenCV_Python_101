import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(0)

lower_red = np.array([20, 130, 0])
upper_red = np.array([255, 160, 200])

while True :
  _, frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  mask = cv2.inRange(hsv, lower_red, upper_red)
  res = cv2.bitwise_and(frame, frame, mask=mask)

  print(mask.shape, res.shape)
  numpy_horizontal = np.hstack((frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), res))
  cv2.imshow('title', numpy_horizontal)
  # cv2.imshow('original', frame)
  # cv2.imshow('mask', mask)
  # cv2.imshow('result', res)

  k = cv2.waitKey(5) 
  if k == ord('q') :
    break

cv2.destroyAllWindows()
cap.release()

  