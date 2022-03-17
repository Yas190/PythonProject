# 10% de comissão em produtos acima de R$20
# O while executa instruções enquanto uma condição for verdadeira
valor = int(input('Valor do produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print (f'A comissão será de R$ %.2f' % valor)
    break
