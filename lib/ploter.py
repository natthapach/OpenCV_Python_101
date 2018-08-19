import matplotlib.pyplot as plt
import lib.flag as Flag
import cv2

class Ploter:

  def __init__(self, row, col):
    self.row = row
    self.col = col
  
  def simple_show(self, images):
    for i in range(len(images)) :
      (img, flag, title) = images[i]
      plt.subplot(self.row, self.col, i+1)

      if(flag == Flag.plt_bgr):
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
      elif(flag == Flag.plt_gray):
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))

      plt.title(title)
      plt.xticks([])
      plt.yticks([])
    plt.show()