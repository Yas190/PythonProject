#Cálculo de média aritmética utilizando listas

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 7:
    notas[x] = float(input(f'Insira a {x +1}° nota: '))
    soma += notas[x]
    x +=1

x = 0

while x < 7:
    print(f'Nota {x +1} : {notas[x]:.2f}')
    x += 1
print(f'A média aritmética das notas é {soma/x:.2f}')