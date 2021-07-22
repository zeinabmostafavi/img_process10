import cv2
img = cv2.imread('pic.jpeg')
row, col, channel = img.shape
for i in range(row):
    for j in range(col):
        if img[i, j][0] < 100 and img[i, j][1] > 110 and img[i, j][2] > 110:
            img[i, j] = [255, 0, 0]
        if img[i, j][0] > 90 and img[i, j][1] > 90 and img[i, j][2] < 100:
            img[i, j] = [0, 0, 255]
        if img[i, j][0] > 50 and img[i, j][1] < 50 and img[i, j][2] > 150:
            img[i, j] = [0, 255, 0]
        if img[i, j][0] > 90 and img[i, j][1] > 90 and img[i, j][2] < 100:
            img[i, j] = [0, 0, 255]
cv2.imshow('result', img)
cv2.waitKey()
