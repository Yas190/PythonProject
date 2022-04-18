# Exemplo de dicionario com estoque e operacoes de venda

estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [100, 1.50]}
venda = [['tomate', 5], ['batata', 10], ['alface', 5]]
total = 0

print('Vendas:\n')
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto}: {quantidade} x {preco:.2f} = {custo:.2f}")
    estoque[produto][0] -= quantidade
    total += custo

print(f"Custo total = {total:.2f}\n")
print("Estoque\n")
for chave, dados in estoque.items():
    print(f"- Descrição:{chave}\n- Quantidade:{dados[0]}\n- Preço:{dados[1]:.2f}\n")
