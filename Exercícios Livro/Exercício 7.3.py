primeira = input('')
segunda = input('')
terceira = ''

for letra in primeira:
    if letra not in segunda and letra not in terceira:
        terceira += letra
for letra in segunda:
    if letra not in primeira and letra not in terceira:
        terceira += letra
        
if terceira == '':
    print('Todos os caracteres são iguais')
else:
    print(f'Caracteres que diferem as strings: {terceira}')