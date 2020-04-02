import cv2
import numpy as np

lena = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(lena)
fshift = np.fft.fftshift(f)

rows, cols = lena.shape
crow,ccol = rows//2 , cols//2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

img_back = img_back/np.max(img_back)*255

cv2.imwrite('result/result.png', img_back)

# salva a imagem dentro da imagem de resultado
#print('result/result.png')
#cv2.imwrite('result/result.png', result)

# (result/np.max(result))*255
# 0 - 1
# print('result/result.png')
# cv2.imwrite('result/result.png', result*255)
