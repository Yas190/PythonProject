T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = T[0]
menor = T[0]
soma = 0

for n in T:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    
print(f'O maior número é {maior}, o menor número é {menor} e a média aritmética é {soma/len(T):.2f}')