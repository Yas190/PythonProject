#Um parâmetro o qual se define um valor --> DEFAULT
#Um parâmetro o qual você não define o valor --> NON DEFAULT
#O parâmetro NON DEFAULT sempre deve vir primeiro

def boas_vindas (quantidade, nome = 'Marcos'):
    print (f'Olá {nome}!')
    print (f'Temos {quantidade} laptops em estoque.')

#No caso, quantidade é NON DEFAULT  e nome é DEFAULT

boas_vindas (6)
