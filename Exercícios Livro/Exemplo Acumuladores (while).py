#Calcular a soma de dez números
n = 1
soma = 0

while n <= 10:
    x = int(input(f'Insira o {n}° número: '))
    soma += x
    n += 1

print(f'A soma dos dez número é igual a {soma}')
