import numpy as np
import cv2
from matplotlib import pyplot as plt
import config

# img = cv2.imread(config.IMG_PATH + 'opencv-python-foreground-extraction-tutorial.jpg')
cap = cv2.VideoCapture(0)
_, img = cap.read()
cap.release()
mask = np.zeros(img.shape[:2],np.uint8)

print(img.shape)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (90,0, 480, 640)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,10,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
res = img*mask2[:,:,np.newaxis]

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.xticks([])
plt.yticks([])
plt.colorbar()

plt.subplot(1, 2,2)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.xticks([])
plt.yticks([])

plt.colorbar()
plt.show()