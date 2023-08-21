import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')

cv2.rectangle(img, (100, 100), (200, 200), (119, 201, 105), thickness=3)

cv2.line(img, (0, img.shape[0] // 2), (img.shape[1], img.shape[0] // 2), (119, 201, 105), thickness=3)

cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 70, (119, 201, 105), thickness=cv2.FILLED)

cv2.imshow('img', img)
cv2.waitKey(0)
