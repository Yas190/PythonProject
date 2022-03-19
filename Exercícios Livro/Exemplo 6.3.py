#Construir a lista com base nos valores de entrada do usuário
lista_numeros = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    lista_numeros[x] = int(input(f'Insira o {x +1}° número: '))
    x += 1

while True:
    selecionado =  int(input('Que posição você gostaria de imprimir? (Se quiser sair, pressione 0):  '))
    if selecionado == 0:
        break
    print(f'A posição {selecionado} corresponde ao número {lista_numeros[selecionado - 1]}')

