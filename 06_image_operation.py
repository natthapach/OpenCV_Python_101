import numpy as np
import cv2
import config


FILE_NAME_1 = config.IMG_PATH + '1.jpg'
FILE_NAME_2 = '2.jpg' 

img1 = cv2.imread(FILE_NAME_1, cv2.IMREAD_COLOR)

# resize
WIDTH = 1280
HEIGHT = 720
img1 = cv2.resize(img1, (WIDTH, HEIGHT))

# extract
# row, col, channel = img1.shape
# roi = img1[0:row, 0:col]

# image must same size
# h
# add = cv2.add(img1, img2)

# grayscale
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# threshold
LOWWER_BOUND = 150
UPPER_BOUND = 255
ret, mask = cv2.threshold(gray, LOWWER_BOUND, UPPER_BOUND, cv2.THRESH_BINARY_INV)

# bitwise
mask_inv = cv2.bitwise_not(mask)
img1_m = cv2.bitwise_and(img1, img1, mask=mask_inv)

# cv2.imshow(TITLE_ADD, add)
cv2.imshow('Gray', gray)
cv2.imshow('Mask', mask)
cv2.imshow('IMG1 Masked', img1_m)

cv2.waitKey(0)
cv2.destroyAllWindows()