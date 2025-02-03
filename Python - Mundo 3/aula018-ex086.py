# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
# matriz na tela, com a formatação correta. ^ 2 1 0 > 0 1 2

matriz = [[],[],[]]
for c in range (0, 3):
    for a in range (0, 3):
        matriz[c].append(int(input(f'Número {c}x{a}: ')))

print('')
for c in range (0, 3):
    for a in range (0, 3):
        print(f'[{matriz[c][a]:^5}]', end='')
    print('')