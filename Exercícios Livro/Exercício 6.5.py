#SIMULAÇÃO DE UMA FILA DE BANCO
#O programa deve ser capaz de ler mais de um comando numa única entrada. Ex.: FFFAAAS

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao final da fila,\nA para realizar o atendimento\nou S para sair.')
    operacao = (input('F, A ou S: ')).upper()
    x = 0

    while x < len(fila):
        if operacao[x] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido!')
            else:
                print('Fila vazia!')
        elif operacao[x] == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == 'S':

            break
        else:
            print('Operação inválida. Digite apena A, F ou S')
        print(f'Fila atual: {fila}')
        x += 1
    if operacao == 'S':
        break
