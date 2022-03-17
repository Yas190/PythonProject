#ATRIBUIÇÃO DE VARIÁVEIS E ENTRADA
#Input: Entrada de dados pelo usuário. Retorna como uma string.

nome = input ('Qual é o seu nome?: ')
idade = input ('Qual é a sua idade?: ')
cidade = input ('Onde você mora?: ')

print(f'Olá, {nome}!\nVocê tem {idade} e mora na cidade de {cidade}!')
print(type(nome))