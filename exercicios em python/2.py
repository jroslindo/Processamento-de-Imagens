'''
Gere a sequência de Fibonacci até um número informado pelo usuário
'''

def main():
    entrada = int(input("numero max"))
    anteriores = [0]*2
    anteriores[0] = 0
    anteriores[1] = 1
    print(0)
    print(1)
    i=0
    while i <= entrada:
        i = anteriores[0] + anteriores[1]
        anteriores[0]=anteriores[1]
        anteriores[1]=i
        if i <= entrada:
            print(i)




main()