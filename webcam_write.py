import numpy as np
import cv2

CAMERA_CHANELL = 0  #index of cemera in computer
cap = cv2.VideoCapture(CAMERA_CHANELL)

FILE_NAME = 'webcam_write_1.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # codex
out = cv2.VideoWriter(FILE_NAME, 0, 20.0, (1280, 720))

WINDOW_TITLE_1 = 'Webcam Color'
WINDOW_TITLE_2 = 'Webcam Gray'

while True:
  ret, frame = cap.read()   # ret is True when read complete, frame is image
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  out.write(frame)
  
  cv2.imshow(WINDOW_TITLE_1, frame)
  cv2.imshow(WINDOW_TITLE_2, gray)


  key = cv2.waitKey(1)
  if key == ord('q'):
    break

cap.release()
out.release()
cv2.destroyAllWindows()