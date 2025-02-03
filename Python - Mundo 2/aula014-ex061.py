# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

termo2, razao2 = termo, razao # Separando as variaveis do ex 061

print('Os 10 primeiros termos dessa PA são:')
for c in range (0, 10):
    termo += razao
    print(f'\033[36m{termo}\033[m', end=' ')

# EX 061
qnt_termo = 0

print('\nOs 10 primeiros termos dessa PA são:')
while qnt_termo != 10:
    qnt_termo += 1
    termo2 += razao2
    print(f'\033[36m{termo2}\033[m', end=' ')