import cv2
import numpy as np

lena = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

TAMANHO_BORDA = 3

# define tamanho da borda que sera ignorado
OFFSET = TAMANHO_BORDA // 2

# define tamanho da imagem resultante
QT_LINHAS_RES = lena.shape[0] - 2 * OFFSET
QT_COLS_RES   = lena.shape[1] - 2 * OFFSET

# cria o array da imagem resultante
result = np.zeros(shape=(
  QT_LINHAS_RES,
  QT_COLS_RES
))
kernel_gauss    = np.array([[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]])
kernel_laplace    = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

# passa pelos elementos da imagem original
for i in range(QT_LINHAS_RES):
  for j in range(QT_COLS_RES):
    acc = 0.
    for k in range(-1, 2):
      for l in range(-1, 2):
        acc += lena[i+OFFSET+k][j+OFFSET+l] * kernel_gauss[k+1][l+1]
    result[i][j] = acc


# passa pelos elementos da imagem original
for i in range(QT_LINHAS_RES):
  for j in range(QT_COLS_RES):
    acc = 0.
    for k in range(-1, 2):
      for l in range(-1, 2):
        acc += lena[i+OFFSET+k][j+OFFSET+l] * kernel_laplace[k+1][l+1]
    result[i][j] = acc

# salva a imagem dentro da imagem de resultado
# print('result/result.png')
cv2.imwrite('result.png', result)

# (result/np.max(result))*255
# 0 - 1
# print('result/result.png')
# cv2.imwrite('result/result.png', result*255)



#conv feita pelo cv2 result = cv2.filter2D (lena, -1, np.array(lp_kernel))