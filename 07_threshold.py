import cv2
import numpy as np
import config
from matplotlib import pyplot as plt

# load image
FILE_NAME = config.IMG_PATH + 'profile1.jpg'
img = cv2.imread(FILE_NAME, cv2.IMREAD_COLOR)

# pre-threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (13, 13), 0)

# threshold
ret1, global_thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

adaptive_thresh_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
adaptive_thresh_gaussian_blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 10)

ret2, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret3, otsu_blur = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

adaptive_thresh_gaussian_otsu = cv2.adaptiveThreshold(otsu, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 1)

# encap image
images = [
  cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
  cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(blur, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(global_thresh, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(adaptive_thresh_mean, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(adaptive_thresh_gaussian, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(adaptive_thresh_gaussian_blur, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(otsu, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(otsu_blur, cv2.COLOR_GRAY2RGB),
  cv2.cvtColor(adaptive_thresh_gaussian_otsu, cv2.COLOR_GRAY2RGB),
]
titles = [
  'original',
  'gray',
  'blur',
  'global\nthreshold',
  'adaptive\nmean',
  'adaptive\ngaussian',
  'adaptive\ngaussian blur',
  'otsu',
  'otsu blur',
  'adaptive gaussian\n otsu'
]

# show output
for i in range(len(images)) :
  plt.subplot(3, 4, (i+1))
  plt.imshow(images[i])
  plt.title(titles[i])
  plt.xticks([])
  plt.yticks([])

plt.show()