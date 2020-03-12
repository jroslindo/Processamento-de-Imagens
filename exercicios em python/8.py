'''
Implemente e plote o Histograma de uma imagem em escala de cinza.
'''
from matplotlib import pyplot as plt
import numpy as np
import cv2

def main ():
    img = cv2.imread("flor.jpg", cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = np.zeros(256)
 
    for  line in gray:
        for pix in line:
            hist[pix] +=1

    plt.plot(hist)


    plt.waitforbuttonpress()


main()