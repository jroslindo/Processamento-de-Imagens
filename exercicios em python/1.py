'''Faça um algoritmo que determine se um número informado pelo usuário é
primo.'''

def main():
    entrada = input("digite um numero para verificar se é primo")

    for i in range(int(entrada)-1):
        i+=1
        print(i)
        if int(entrada) % i ==0 and (i != 1 and i !=int(entrada)):
            print("não é primo")
            return
            

    print("é primo")
        

main()


