# contar letras repetidas
teste = input('')
for letra in teste:
    p = teste.count(letra)
    print(f'{letra}: {p}x')