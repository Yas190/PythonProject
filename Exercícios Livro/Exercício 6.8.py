#Pesquisar se um determinado valor se encontra dentro da lista
lista = [1, 4, 9, 16, 25, 36, 49, 64, 81]
valor_um = int(input('Primeiro valor que deseja encontrar: '))
valor_dois = int(input('Segundo valor que deseja encontrar: '))
x = 0

while x < len(lista):
    if lista[x] == valor_um:
        break
    x += 1

if x < len(lista):
    print(f'Este valor foi encontrado na posição {x}!')
else:
    print('Valor não encontrado.')