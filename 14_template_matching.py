import numpy as np
import cv2
import matplotlib.pyplot as plt
import config

img1 = cv2.imread(config.IMG_PATH + 'feature_match_1-1.jpg',0)
img2 = cv2.imread(config.IMG_PATH + 'feature_match_1-2.jpg',0)
img3 = cv2.imread(config.IMG_PATH + 'feature_match_1-3.jpg',0)

color1 = cv2.imread(config.IMG_PATH + 'feature_match_1-1.jpg', cv2.IMREAD_COLOR)
color2 = cv2.imread(config.IMG_PATH + 'feature_match_1-2.jpg', cv2.IMREAD_COLOR)
color3 = cv2.imread(config.IMG_PATH + 'feature_match_1-3.jpg', cv2.IMREAD_COLOR)


orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
kp3, des3 = orb.detectAndCompute(img3, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches12 = bf.match(des1,des2)
matches12 = sorted(matches12, key = lambda x:x.distance)
matches13 = bf.match(des1,des3)
matches13 = sorted(matches13, key = lambda x:x.distance)

res1 = cv2.drawMatches(color1,kp1,color2,kp2,matches12[:20],None, flags=2)
res2 = cv2.drawMatches(color1,kp1,color3,kp2,matches13[:20],None, flags=2)

print(len(matches12))
print(len(matches13))

plt.subplot(2, 1, 1)
plt.imshow(cv2.cvtColor(res1, cv2.COLOR_BGR2RGB))
plt.xticks([])
plt.yticks([])

plt.subplot(2, 1, 2)
plt.imshow(cv2.cvtColor(res2, cv2.COLOR_BGR2RGB))
plt.xticks([])
plt.yticks([])

plt.show()