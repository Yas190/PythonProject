#Exibir valor da pupança em 24 meses com base no valor inicial e na taxa de juros. Imprimir total ganho nesses 24 meses
deposito_inicial = float(input('Insira o valor do depósito inicial: R$'))
taxa = float(input('Insira a taxa de juros, em %: '))
saldo = deposito_inicial
mes = 1

while mes <= 24:
    saldo = saldo + (taxa/100 * saldo)
    print(f'Seu saldo no mês {mes} é de R${saldo:.2f}')
    mes += 1

print(f'Seu ganho total com a poupança para este período foi de R${saldo - deposito_inicial:.2f}')