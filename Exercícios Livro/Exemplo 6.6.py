#Adição de elementos à lista


lista = []

while True:
    numero = int(input('Insira uma número ou pressione 0 para sair: '))
    if numero == 0:
        break
    lista.append(numero)

x = 0

while x < len(lista):
    print(lista[x])
    x += 1