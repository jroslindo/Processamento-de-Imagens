import cv2
import numpy as np

lena = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

sob_x = np.array([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1],
])

sob_y = np.array([
  [ 1,  2,  1],
  [ 0,  0,  0],
  [-1, -2, -1],
])

res_x = cv2.filter2D(lena, -1, sob_x)
res_y = cv2.filter2D(lena, -1, sob_y)

res = np.sqrt(res_x**2 + res_y**2)

res = res / np.max(res) * 255

print('result/result.png')
cv2.imwrite('result/result.png', res.astype(np.float32))
