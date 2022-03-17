
while True:
    print('[1] Adição \n[2] Subtração \n[3] Divisão \n[4] Multiplicação \n[0] Sair')
    c = int(input('Insira o número desejado de acordo com o menu: '))

    if c == 0:
        break

    elif 1 <= c < 5:
        n = int(input('Tabuada de: '))
        x = 1
        while x <= 10:
            if c == 1:
                print(f'{n} + {x} = {n + x}')
            elif c == 2:
                print(f'{n} - {x} = {n - x}')
            elif c == 3:
                print(f'{n} : {x} = {n / x}')
            elif c == 2:
                print(f'{n} x {x} = {n * x}')
            x += 1
    else:
        print('Comando Inválido')