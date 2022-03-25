# Colocar elementos da lista em ordem decrescente através do Bubble Sort

L = [1, 2, 3, 4, 5]
fim = 5

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x + 1]:
            trocou = True
            var_aux = L[x]
            L[x] = L[x + 1]
            L[x + 1] = var_aux
        x += 1
    if not trocou:
        break
    fim -= 1
for n in L:
    print(n)