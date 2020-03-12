'''
Implemente o Bubble Sort utilizando listas do Python.
'''

def main():
    vet = [9,1,3,2,6,4,5,7,0,-4,2,-3]
    aux = 0
    while True:
        para = True
        for i in range(len(vet)-1):
            if vet[i] > vet[i+1]:
                aux = vet[i]
                vet[i] = vet[i+1]
                vet[i+1]= aux
                para = False
        if para == True:
            break

    print (vet)





main()