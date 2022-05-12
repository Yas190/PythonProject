# ler duas string e verificar se a segunda ocorre na primeira
primeira = input('')
segunda = input('')
terceira = ''
for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == '':
    print('Caracteres em comum não encontrados')
else:
    print(f'Caracteres em comum {terceira}')