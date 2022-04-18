# Exemplo de dicionario com estoque e operacoes de venda com entrada de usuario

estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [100, 1.50]}

total = 0

print("Vendas\n")
while True:
    produto = input('Insira o nome do produto ou fim para sair: ')
    if produto == 'fim':
        break
    elif produto in estoque:
        quantidade = int(input('Insira a quantidade do produto: '))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = quantidade * preco
            print(f"{produto}: {quantidade} x {preco:.2f} = {custo:.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print('Quantidade solicitada não disponível.')
    else:
        print("Produto não consta no estoque")

print(f'Custo total:{total:.2f}')
print('Estoque\n')
for chaves, dados in estoque.items():
    print(f'Descrição:{chaves}\nQuantidade:{dados[0]}\nPreço:{dados[1]}\n')