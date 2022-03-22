#Verificando o menor valor

lista = [2, 7, 1, 0, 6, 2, 1, -5, -10]
menor = lista[1]

for n in lista:
    if n < menor:
        menor = n

print(menor)