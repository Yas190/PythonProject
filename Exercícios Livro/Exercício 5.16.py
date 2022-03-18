#Imprimir a quantidade de cédulas necessárias para pagar um determinado valor

valor = int(input('Digite o valor a ser pago: '))
quantidade_cedulas = 0
valor_atual_cedula = 50
apagar = valor

while True:
    if valor_atual_cedula <= apagar:
        apagar -= valor_atual_cedula
