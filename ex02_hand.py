import cv2
import numpy as np

cap_front = cv2.VideoCapture(0)
cap_side = cv2.VideoCapture(1)

while cv2.waitKey(5) != ord('q') :
  _, front = cap_front.read()
  _, side = cap_side.read()

  edge_front = cv2.Canny(front, 100, 180)
  edge_side = cv2.Canny(side, 100, 180)

  cv2.imshow('front', front)
  cv2.imshow('side', side)
  cv2.imshow('front-edge', edge_front)
  cv2.imshow('side-edge', edge_side)

cv2.destroyAllWindows()
cap_front.release()
cap_side.release()