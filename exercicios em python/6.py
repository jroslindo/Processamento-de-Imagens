'''
Implemente a subtração de matrizes utilizando array do Numpy.
'''
import numpy as np



def main():
    mat1 = np.matrix("10 9 8 7;6 5 4 3")
    mat2 = np.matrix("6 5 4 3; 10 9 8 7")
    resp= np.matrix("0 0 0 0;0 0 0 0")


    for i in range(2):
        for j in range(len(mat1[1])):
            resp[i][j] = mat1[i][j] - mat2[i][j]

    print(resp)

main()