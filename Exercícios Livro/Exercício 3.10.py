salario_antigo = float(input('Insira o valor do seu salário atual: R$'))
porcentagem_aumento = float(input('Insira a porcentagem de aumento do seu salário: '))
valor_aumento = (porcentagem_aumento/100) * salario_antigo
salario_atual = valor_aumento + salario_antigo

print(f'Seu aumento corresponde ao valor de R${valor_aumento:.2f}, portanto, seu salário atual é de {salario_atual:.2f}')

