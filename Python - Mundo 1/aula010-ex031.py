# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrabando
# 50 cents por km para viagens de até 200km e 45 cents para viagens mais longas.

km = int(input('Qual a kilometragem rodada? '))
if km <= 200:
    print(f'O seu aluguel é de R$ {float(km*.5):.2f}')
else:
    print(f'O seu aluguel é de R$ {float(km*.45):.2f}')

print('Boa viagem!')