# Ler um número e imprimir todos os números anteriores a entrada do usuário

N = int(input('Insira um número: '))

for numero in range (N):
    print (numero+1, end=' ')