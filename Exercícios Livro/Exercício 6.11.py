#Imprimir uma lista, que possua o índice entre colchetes e o seu valor correspondente

#Utilizando o FOR
'''
lista = [2, 4, 6, 8]
x = 0
for n in L:
    print(f'[{x}]: {n}')
    x += 1
'''

#Utilizando o ENUMERATE
lista = [2, 4, 6, 8]
for x, n in enumerate(lista):
    print(f'[{x}]: {n}')
