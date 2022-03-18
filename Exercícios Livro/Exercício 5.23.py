#Verificar se um número é primo

numero = int(input('Insira um número: '))

if numero < 1:                  #Se número for menor que 1
    print('Numero inválido')    #Se número for 0 ou 1
if numero == 0 or numero == 1:
    print('Caso especial')
else:
    if numero == 2:             #Se for igual a 2
        print('Primo')
    elif numero % 2 == 0:       #Um número par, além do 2
        print('Não é primo')
    else:
        x = 3
        while (x < numero):     #Enquanto a sequencia de numero for menor do que o numero
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print('Primo')
        else:
            print(f'{numero} não é primo porque é divisível por {x}')

            




