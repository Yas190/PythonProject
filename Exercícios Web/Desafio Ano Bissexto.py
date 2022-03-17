#Ler um ano e imprimir se é bissexto ou não

ano = int (input('Insira um ano e confira se ele é bissexto: '))
ano_bissexto = True
ano_normal = False
#Condições para ser bissexto: divisível por 4, não pode ser divisível por 100 e pode ser divisível por 400
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
   print(ano_bissexto)
   print(f'{ano} é bissexto')

else:
    print (ano_normal)
    print(f'{ano} não é bissexto')