#DESAFIO ÍMPAR E PAR
#Utilizando operadores lógicos
#Se n° for par e menor igual que 5, print 'Not weird'
#Se n° for par, maior que 5 e menor que 20, print 'Weird'
#Se n° for par, maior que 20, print 'Not weird'
#Se n° for ímpar, print 'Weird'

n = int(input ('Insira um número: '))
r = n % 2
if (r == 0) and (n >= 2) and (n <= 5):
    print ('Not Weird')
elif (r == 0) and (n >= 6) and (n <= 20):
    print ('Weird')
elif (r == 0) and (n > 20):
    print ('Not Weird')
else:
    print ('Weird')