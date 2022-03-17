#Calcular o preço do aluguel de um carro sabendo que a diária é 60 reias e o quilômetro rodado é 0.15 reais
dias = int(input('Insira a quantidade de dias em que o carro foi alugado: '))
quilometros = float(input('Insira a quantidade de quilômetros rodados: '))
diaria = 60 * dias
preco_km = quilometros * 0.15
preco_total = diaria + preco_km

print(f'O preço a pagar será de {preco_total}')