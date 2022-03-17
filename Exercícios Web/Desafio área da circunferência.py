#DESAFIO: CÁLCULO DA ÁREA DA CIRCUNFERÊNCIA
#Utilizando operadores de atribuição

raio = float(input('Raio da circunferência, em metros quadrados: '))
raio *= raio
area = round(raio * 3.14159, 2)

#Round: retorna o float arreddondado, sendo o número de decimais especificado

print (f'A área da circunferência corresponde a {area} metros quadrados!')