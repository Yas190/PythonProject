# Classificar uma lista com base em quão próximo o número está de 50

def my_function(n):
    return abs(n - 50)

list = [100, 50, 65, 82, 23]

list.sort(key = my_function)
print(list)
