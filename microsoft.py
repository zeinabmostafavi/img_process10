import cv2
import numpy as np

h = 300
w = h*2
img = np.full((h, w, 3), 80, dtype="uint8")
img[100:145, 100:145] = [0, 60, 255]
img[100:145, 155:200] = [0, 255, 0]
img[155:200, 100:145] = [255, 150, 0]
img[155:200, 155:200] = [0, 200, 255]
img = cv2.putText(img, 'Microsoft', (210, 170),
                  cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)
cv2.imshow('out', img)
cv2.imwrite('Microsof.png', img)
cv2.waitKey()
