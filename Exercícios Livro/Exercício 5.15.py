'''
Escreva um programa para controlar uma pequena máquina regist
Você deve solicitar ao usuário que digite o código do produto e a
quantidade comprada.
'''

soma = 0

while True:
    p = float(input('Insira o código do produto: '))
    if p == 0:
        break
    elif p == 1:
        preco = 0.5
    elif p == 2:
        preco = 1
    elif p == 3:
        preco = 4
    elif p == 5:
        preco = 7
    elif p == 9:
        preco = 8
    else:
        print('Código inválido')
    if preco != 0:
        quantidade = int(input('Quantidade comprada: '))
        soma = soma + (preco * quantidade)

print(f'O total da compra será de {soma:.2f}')

