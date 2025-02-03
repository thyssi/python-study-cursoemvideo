# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

km = int(input('Informe a velocidade do veículo: '))
if km>80:
    print(f'Você foi multado. O valor da sua multa é de R${(float(km-80)*7):.2f}')
else:
    print('Safe! Você está dentro da velocidade permitida.')