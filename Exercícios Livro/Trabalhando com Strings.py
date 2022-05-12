# Separar caracteres de uma string
string = "Olá, Mundo!"
lista = list(string)
print(list)
# Alterando caractere
lista[5] = 'm'
print(lista)
# Reunindo caracteres
string2 = ''.join(lista)
print(string2)

# Verificação de string
nome = 'João dos Santos'
print(nome.startswith('João'))
print(nome.startswith('joão'))
print(nome.endswith('Santos'))
print('dos Santos' in nome)
print('Cezere' not in nome)

# Contar letra ou palavra
s = 'um tigre, dois tigres, três tigres'
print(s.count('tigre'))

# Pesquisa em string
print(s.find('tigre')) # Retorna index com 1° caractere da string procurada
print(s.rfind('três')) # da direita para a esquerda
print(s.find('quatro')) # Retorno negativo

# Posicionamento em string
a = 'tigre'
print(a.center(15, '.'))
print(a.ljust(15, '.'))
print(a.rjust(15, '.'))