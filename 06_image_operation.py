import numpy as np
import cv2

FILE_NAME_1 = '1.jpg'
FILE_NAME_2 = '2.jpg'

img1 = cv2.imread(FILE_NAME_1, cv2.IMREAD_COLOR)
img2 = cv2.imread(FILE_NAME_2, cv2.IMREAD_COLOR)

print(img1.shape)
print(img2.shape)
cv2.imshow('xxx', img1)
cv2.imshow('yyy', img2)
add = cv2.add(img2, img2)

TITLE_ADD = 'Add'
cv2.imshow(TITLE_ADD, add)
cv2.waitKey(0)
cv2.destroyAllWindows()