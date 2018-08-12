import cv2
import numpy as np
import config

FILE_NAME = config.IMG_PATH + '1.jpg'
img = cv2.imread(FILE_NAME, cv2.IMREAD_COLOR)

# img[y1:y2, x1:x2]
# select part of image
roi = img[0:500, 0:500]   # region of image

# change part of image
img[0:500, 500:1000] = [255, 255, 255]

# # paste image part
img[500:1000, 500:1000] = img[500:1000, 0:500]

WINDOW_TITLE_1 = 'ROI'
WINDOW_TITLE_2 = 'Change'
cv2.imshow(WINDOW_TITLE_1, roi)
cv2.imshow(WINDOW_TITLE_2, img)

cv2.waitKey(0)
cv2.destroyAllWindows()