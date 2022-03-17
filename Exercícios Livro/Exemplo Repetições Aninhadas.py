produto_fixo = 1

while produto_fixo <= 10:
    produto_variavel = 1
    while produto_variavel <= 10:
        print(f'{produto_fixo} x {produto_variavel} = {produto_fixo * produto_variavel}')
        produto_variavel += 1
    produto_fixo += 1
    print('---------------')