# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos dessa PA são:')
for c in range (0, 10):
    termo += razao
    print(f'\033[36m{termo}', end=' ')