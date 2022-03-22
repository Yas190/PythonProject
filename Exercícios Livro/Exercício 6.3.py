#Leia duas listas e gere uma terceira lista com os elementos das duas primeiras
lista_1 = []
lista_2 = []


while True:
    numero = int(input('Insira os números da primeira lista (Pressione 0 para parar): '))
    if numero == 0:
        break
    lista_1.append(numero)

while True:
    numero = int(input('Insira os números da segunda lista (Pressione 0 para parar): '))
    if numero == 0:
        break
    lista_1.append(numero)


lista_1.extend(lista_2)
duas_listas = lista_1[:]                    #AS DUAS LISTAS VIRAM UMA SÓ, COM REPETIÇÕES
lista_3 = []                                #CRIAÇÃO DA TERCEIRA LISTA, VAZIA
x = 0                                       #VAMOS PERCORRER A DUAS_LISTAS

while x < len(duas_listas):
    y = 0
    while y < len(lista_3):
        if duas_listas[x] == lista_3[y]:
            break
        y += 1
    if y == len(lista_3):
        lista_3.append(duas_listas[x])
    x += 1

x = 0

while x < len(lista_3):
    print(f'{x + 1}°: {lista_3[x]}')
    x += 1


