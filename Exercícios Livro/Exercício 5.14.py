'''
Escreva um programa que leia números inteiros do teclado. O programa
deve ler os números até que o usuário digite 0 (zero). No final da
execução, exiba a quantidade de números digitados, assim como a soma e
a média aritmética.
'''

posicao = 0
soma = 0

while True:
    v  = int(input(f'Insira o {posicao + 1}° número:'))
    if v == 0:
        break
    soma += v
    posicao += 1

print(f'Você digitou {posicao} números. A soma dos números resulta em {soma} e a média aritmética é igual a {soma/posicao:.2f}')

