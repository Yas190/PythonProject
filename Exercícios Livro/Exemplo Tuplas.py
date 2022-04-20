tupla = 'a', 'b', 'c'  # empacotamento
print(tupla)

tupla2 = ('a', 'b', 'c')
print(f'{tupla2}\n')

a, b = 10, 20  # desempacotamento
print(a)
print(f'{b}\n')

a, b = b, a
print(a)
print(f'{b}\n')
# tuplas com um elemento
tupla3 = 1,
print(tupla3)

tupla4 = (1,)
print(tupla4)

tupla5 = ()
print(len(tupla5))
print('')
tupla6 = (1, 2, ['a', 'b', 'c', 'd'])
tupla6[2].append('e')
print(tupla6)

lista = [1, 2, 3, 4]
print(tuple(lista))
print('')
# desempacotamento com *
a, *b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)