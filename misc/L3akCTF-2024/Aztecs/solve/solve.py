import numpy as np
import cv2

#画像を読み込む
original = cv2.imread('challenge.png')
height, width, channel = original.shape[:3]

size = (height, width)
greenshare = np.zeros(size, np.uint8)
redshare = np.zeros(size, np.uint8)
blueshare = np.zeros(size, np.uint8)

for h in range(height):
    for w in range(width):
        if original[h][w][0] == 255:
            greenshare[h][w] = 255
        if original[h][w][1] == 255:
            redshare[h][w] = 255
        if original[h][w][2] == 255:
            blueshare[h][w] = 255

cv2.imwrite('greenshare.png', greenshare)
cv2.imwrite('redshare.png', redshare)
cv2.imwrite('blueshare.png', blueshare)
