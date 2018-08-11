import cv2
import numpy as np
import matplotlib as plt

IMAGE_NAME = '1.jpg'
image_obj_1 = cv2.imread(IMAGE_NAME, cv2.IMREAD_GRAYSCALE)  # open image in gray scale
image_obj_2 = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)  # open image in color mode

WINDOW_IMAGE_TITLE = 'image'
cv2.imshow(WINDOW_IMAGE_TITLE, image_obj_1)

cv2.waitKey(0)
cv2.destroyAllWindows()