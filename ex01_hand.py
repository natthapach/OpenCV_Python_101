import cv2
import numpy as np
import config
import matplotlib.pyplot as plt
from lib.ploter import Ploter
import lib.flag as Flag

# initial
img_side = cv2.imread(config.IMG_PATH + 'hand_side - 2.jpg', cv2.IMREAD_COLOR)
img_front = cv2.imread(config.IMG_PATH + 'hand_front - 2.jpg', cv2.IMREAD_COLOR)
ploter = Ploter(2, 2)

edge_side = cv2.Canny(img_side, 100, 150)
edge_front = cv2.Canny(img_front, 100, 120)

images = [
  (img_side, Flag.plt_bgr, 'origin side'),
  (img_front, Flag.plt_bgr, 'origin front'),
  (edge_side, Flag.plt_gray, 'edge side'),
  (edge_front, Flag.plt_gray, 'edge front'),
]

ploter.simple_show(images)

