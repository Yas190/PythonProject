#Uma função é capaz de armazenar um conjunto de dados e pode ser executada sempre que for chamada
#A função pode receber parâmetros. Os parâmetros recebem os argumentos correspondentes na chamada da função
#Uma função deve ser chamada com o número correto de argumentos
  #No caso, foram chamados dois argumentos para dois parâmetros já definidos

def boas_vindas (nome, quantidade):
    print (f'Olá {nome}!')
    print (f'Temos {quantidade} laptops em estoque.')

boas_vindas ('Marcos', 5)
boas_vindas ('Ana', 4)