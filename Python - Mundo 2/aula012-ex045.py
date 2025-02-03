# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

num_pc = choice(['pedra', 'papel', 'tesoura'])
user = str(input('Pedra, papel ou tesoura? '))
num_user = user.strip().lower()
vitoria, derrota = 'Você ganhou!', 'Você perdeu!'

print(f'Eu joguei {num_pc}.', end=' ')
if num_pc == num_user:
    print('Empate.')
elif num_pc == 'pedra':
    if num_user == 'papel':
        print(vitoria)
    else:
        print(derrota)
elif num_pc == 'papel':
    if num_user == 'pedra':
        print(derrota)
    else:
        print(vitoria)
else:
    if num_user == 'papel':
        print(derrota)
    else:
        print(vitoria)