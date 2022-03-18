#Se você não souber quantos argumentos de palavra-chave serão passados para sua função,
# adicione  ** antes do nome do parâmetro na definição da função.

#Desta forma a função receberá um dicionário de argumentos, podendo acessar os itens de acordo

def agencia(**carro):
    return carro

print (agencia(marca = 'Gol', cor = 'Vermelho', motor = 1.0))
print (agencia(marca = 'Gol', cor = 'Azul', motor = 1.0, placa = 4444))
print (agencia(marca = 'Gol', cor = 'Preto'))