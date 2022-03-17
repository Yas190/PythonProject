
#Calcular o tempo de viagem com base na distância e velocidade dadas pelo usuário

distancia = float(input('Insira a distância a ser percorrida, em Km: '))
velocidade = float(input('Qual a velocidade média esperada para a viagem, em Km/h?: '))
tempo = round(distancia / velocidade, 2)
tempo_horas = int((tempo * 60) // 60)
tempo_minutos = int((tempo * 60) % 60)

if tempo_minutos == 0:
    print(f'O tempo de viagem será de aproximadamente {tempo_horas} hora.')
else:
    print(f'O tempo de viagem será de aproximadamente {tempo_horas} horas e {tempo_minutos} minutos.')
