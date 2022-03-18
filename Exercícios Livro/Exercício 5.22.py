print('[1] Adição \n[2] Subtração \n[3] Divisão \n[4] Multiplicação \n[0] Sair')
c = int(input('Insira o número desejado de acordo com o menu: '))

while True:
    if c == 0:
        break

    elif c == 1:
        soma_fixo = 1
        while soma_fixo <= 10:
            soma_variavel = 1
            while soma_variavel <= 10:
                print(f'{soma_fixo} + {soma_variavel} = {soma_fixo + soma_variavel}')
                soma_variavel += 1
            soma_fixo += 1
            print('---------------')
        break

    elif c == 2:
        sub_fixo = 1
        while sub_fixo <= 10:
            sub_variavel = 1
            while sub_variavel <= 10:
                print(f'{sub_fixo} - {sub_variavel} = {sub_fixo - sub_variavel}')
                sub_variavel += 1
            sub_fixo += 1
            print('---------------')
        break

    elif c == 3:
        dividendo = 1
        while dividendo <= 10:
            divisor = 1
            while divisor <= 10:
                print(f'{dividendo} : {divisor} = {dividendo / divisor}')
                divisor += 1
            dividendo += 1
            print('---------------')
        break

    elif c == 4:
        produto_fixo = 1
        while produto_fixo <= 10:
            produto_variavel = 1
            while produto_variavel <= 10:
                print(f'{produto_fixo} x {produto_variavel} = {produto_fixo * produto_variavel}')
                produto_variavel += 1
            produto_fixo += 1
            print('---------------')
        break