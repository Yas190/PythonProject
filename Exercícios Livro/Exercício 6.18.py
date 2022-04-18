# Programa para gerar um dicionário a partir de uma frase lida em que cada frase é um caractere e seu
# valor e a quantidade de vezes em que ele aparece

frase = input('Insira uma frase para formar o dicionário: ')
d = {}

for letra in frase:
    if letra in d:
        d[letra] += 1
    else:
        d[letra] = 1

del d[' ']
print(d)