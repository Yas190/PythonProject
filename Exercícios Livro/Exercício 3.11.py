#Solicitar preço de uma mercadoria e desconto aplicado
#Imprimir valor do desconto e preço final da mercadoria

preco_mercadoria = float(input('Insira o valor da mercadoria: R$'))
percentual_desconto = float(input('Insira o percentual de desconto, em %: '))
valor_desconto = (percentual_desconto/100) * preco_mercadoria
preco_com_desconto = preco_mercadoria - valor_desconto

print(f'O valor do desconto será de R${valor_desconto:.2f}, portanto, o preço da mercadoria com desconto será de R${preco_com_desconto:.2f}')