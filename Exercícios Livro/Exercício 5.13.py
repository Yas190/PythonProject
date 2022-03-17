'''
Escreva um programa que pergunte o valor inicial de uma dívida e o
mensal. Pergunte também o valor mensal que será pago. Imprima o
número de meses para que a dívida seja paga, o total pago e o total
juros pago.
'''

divida = float(input('Insira o valor da dívida: R$'))
juro_mensal = float(input('Insira o valor do juro mensal sobre a dívida, em %: '))
valor_mensal_pago = float(input(f'Insira o valor mensal que será pago: R$'))
mes = 1

if  juro_mensal/100 * divida > valor_mensal_pago:
    print('Para esse valor mensal, suas dívidas nunca serão pagas, já que ele é inferior aos juros')
else:
   saldo = divida
   juros_pagos = 0
   while saldo > valor_mensal_pago:                  #Enquanto a dívida for maior que pagamento mensal
       juros = juro_mensal/100 * saldo              #Juro mensal da dívida
       saldo = saldo + juros - valor_mensal_pago     #Dívida com juros descontando pagamento mensal
       juros_pagos = juros_pagos + juros             #Juros pagos
       print(f'Saldo da dívida no mês {mes} é de R${saldo:.2f}')
       mes += 1

print(f'São necessários {mes - 1} meses para pagar a dívida. O total pago será de R${divida + juros_pagos:.2f} e o total de juros pagos será de R${juros_pagos:.2f}')







