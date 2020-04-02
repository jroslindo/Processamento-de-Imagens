import cv2
import numpy as np

lena = cv2.imread('lena.png', cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(lena, cv2.COLOR_BGR2HSV)

lower_blue = np.array([0,0,0])
upper_blue = np.array([5,255,255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(lena, lena, mask=mask)

print('result/result.png')
cv2.imwrite('result/result.png', res)
