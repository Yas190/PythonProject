sequencia = input('Digite a sequência de parênteses a validar: ')
pilha = []
x = 0

while x < len(sequencia):
    if sequencia[x] == '(':
        pilha.append('(')
    if sequencia[x] == ')':
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(')')
            break
    x += 1

if len(pilha) == 0:
    print('OK')
else:
    print('Erro')

