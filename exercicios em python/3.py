'''
Calcule a média aritmética de uma quantidade indeterminada de números
informados pelo usuário. Considere, como critério de parada, o usuário digitar a
letra n ao invés de um número.
'''

def main():
    vet=[]
    i=0
    while i != 'n':
        i = input("digite um numero, n faz parar")
        if i!='n':
            vet.append(int(i))
    soma = 0
    print(vet)
    for valor in vet:
        soma += valor
    print("media" + str(soma/len(vet)))



main()