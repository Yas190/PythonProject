#Se você não souber quantos argumentos serão passados para sua função,
# adicione um * antes do nome do parâmetro na definição da função

#Soma de uma quantidade de números indeterminada

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

print (soma(2,3,4,7))