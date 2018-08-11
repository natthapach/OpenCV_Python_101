import cv2
import numpy as np


RED = 255
GREEN = 255
BLUE = 255

# open image
IMAGE_NAME = '1.jpg'
image_obj = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)

# draw line
PL1 = (0, 0)
PL2 = (150, 150)
COLOR_L = (RED, 0, 0)
WIDTH_L = 10
cv2.line(image_obj, PL1, PL2, COLOR_L, WIDTH_L)

# draw rectangle
PR_LT = (150, 150)    # left-top point
PR_RB = (300, 300)    # right-bottom point
COLOR_R = (0, GREEN, 0)
WIDTH_R = 5
cv2.rectangle(image_obj, PR_LT, PR_RB, COLOR_R, WIDTH_R)

# draw circle
PC_CENTER = (225, 225)
RADIUS = 75
COLOR_C = (0, 0, BLUE)
WIDTH_C = -1    # fill color
cv2.circle(image_obj, PC_CENTER, RADIUS, COLOR_C, WIDTH_C)

# draw polygon
PYs = np.array([[300, 300,], [458, 500], [600, 628], [700, 400]], np.int32)
COLOR_Y = (RED, GREEN, 0)
WIDTH_Y = 5
IS_CONNECT_LAST_POINT = False
cv2.polylines(image_obj, [PYs], IS_CONNECT_LAST_POINT, COLOR_Y, WIDTH_Y)

# draw text
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SIZE = 3
TEXT = 'Hello World OpenCV'
PT_LB = (150, 150)  # left-bottom
COLOR_T = (0, 0, 0)
WIDTH_T = 3
LINE_TYPE_1 = cv2.LINE_AA  # make text from array of line
LINE_TYPE_2 = cv2.LINE_8    # make text from array of rectangle
cv2.putText(image_obj, TEXT, PT_LB, FONT, FONT_SIZE, COLOR_T, WIDTH_T, LINE_TYPE_1)

# show image
TITLE = 'image'
cv2.imshow(TITLE, image_obj)
cv2.waitKey(0)
cv2.destroyAllWindows()