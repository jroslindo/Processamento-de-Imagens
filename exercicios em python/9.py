'''
Implemente a operação morfológica de erosão (elemento estruturante 3x3) em
uma imagem binária utilizando array do Numpy. Ignore as bordas.
'''
import numpy as np
import random

def main():
    mat = np.zeros((20,20))
    for linha in range(len(mat[0])):
        for coluna in range(len(mat[0])):
            mat[linha][coluna] = random.randint(0, 1)
    
    kernel = np.matrix('1 1 1; 1 1 1; 1 1 1')
    resposta = np.zeros((20,20))
    
    i = 1
    while i < len(mat[0])-1:
        j=1
        while j < len(mat[0])-1:
            if(mat[i-1][j-1]) and kernel [0][0])and




            j+=1
        i+=1
    print(mat)


main()