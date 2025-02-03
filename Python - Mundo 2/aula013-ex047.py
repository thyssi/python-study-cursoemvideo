# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('\033[32;4mSegue abaixo a lista de números pares que estão entre 1 e 50:\033[m')
for c in range (0, 50, 2):
    print('.', end=' ')
    print(c, end=' ')