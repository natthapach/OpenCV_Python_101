import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(1)

while(True):
  _, frame = cap.read()

  blur = cv2.GaussianBlur(frame, (15, 15), 10)

  laplacian = cv2.Laplacian(frame,cv2.CV_64F)
  laplacian_b = cv2.Laplacian(frame, cv2.CV_64F)
  sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
  sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
  edges = cv2.Canny(frame, 100, 180)

  cv2.imshow('Original',frame)
  cv2.imshow('laplacian',laplacian)
  cv2.imshow('laplacian blur', laplacian_b)
  cv2.imshow('sobelx',sobelx)
  cv2.imshow('sobely',sobely)
  cv2.imshow('edges', edges)

  k = cv2.waitKey(5)
  if k == ord('q'):
      break

cv2.destroyAllWindows()
cap.release()