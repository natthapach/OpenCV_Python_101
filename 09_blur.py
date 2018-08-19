import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_red = np.array([20, 120, 0])
upper_red = np.array([255, 160, 190])

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((15, 15), np.float32)/500
    smoothed = cv2.filter2D(res, -1, kernel)
    
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bil

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Res', res)
    cv2.imshow('Smoothed', smoothed)

    k = cv2.waitKey(5)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()