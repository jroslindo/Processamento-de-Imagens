import cv2
import numpy as np
from skimage.util import random_noise
from skimage import metrics

lena = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

img_ruido = random_noise(lena, mode='s&p',amount=0.2)

TAMANHO_BORDA = 3

# define tamanho da borda que sera ignorado
OFFSET = TAMANHO_BORDA // 2 

# define tamanho da imagem resultante
QT_LINHAS_RES = img_ruido.shape[0] - 2 * OFFSET
QT_COLS_RES   = img_ruido.shape[1] - 2 * OFFSET

# cria o array da imagem resultante
result = np.zeros(shape=(
  QT_LINHAS_RES,
  QT_COLS_RES
))

gauss_kernel = [
  [1/16, 1/8, 1/16],
  [1/8,  1/4, 1/8],
  [1/16, 1/8, 1/16]
]

# passa pelos elementos da imagem original
for i in range(QT_LINHAS_RES):
  for j in range(QT_COLS_RES):
    acc = 0.
    for k in range(-1, 2):
      for l in range(-1, 2):
        acc += img_ruido[i+OFFSET+k][j+OFFSET+l] * gauss_kernel[k+1][l+1]
    result[i][j] = acc

# salva a imagem dentro da imagem de resultado
# print('result/img_ruido.png')
cv2.imwrite('img_ruido.png', img_ruido*255)

# salva a imagem dentro da imagem de resultado
# print('result/result.png')
cv2.imwrite('result.png', result*255)

# (result/np.max(result))*255
# 0 - 1
# print('result/result.png')
# cv2.imwrite('result/result.png', result*255)


# analise das imagens
print("PSNR")
print(" ruidos: ", metrics.peak_signal_noise_ratio(
  lena,
  (img_ruido*255).astype(np.uint8))
)
print(" gauss: ", metrics.peak_signal_noise_ratio(
  lena[1:-1, 1:-1],
  (result*255).astype(np.uint8))
)



