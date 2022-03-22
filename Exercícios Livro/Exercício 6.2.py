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

print(lista_1)