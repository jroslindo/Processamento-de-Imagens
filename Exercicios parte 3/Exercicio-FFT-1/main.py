import cv2
import numpy as np

lena = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(lena)
fshift = np.fft.fftshift(f) #objetivo de mudar a posiçao daas componentes 0
magnitude_spectrum = 20*np.log(np.abs(fshift)) #em decibeis

cv2.imwrite('result/magnitude.png', magnitude_spectrum)

# salva a imagem dentro da imagem de resultado
#print('result/result.png')
#cv2.imwrite('result/result.png', result)

# (result/np.max(result))*255
# 0 - 1
# print('result/result.png')
# cv2.imwrite('result/result.png', result*255)
