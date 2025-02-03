# Faça um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Informe a medida da 1° reta: '))
b = float(input('Da 2°: '))
c = float(input('Da 3°: '))

if (b-a) < c < (b+a) and (a-c) < b < (a+c) and (c-b) < a < (c+b):
    print(f'Sim, {a}, {b} e {c} formam um triângulo.')
else:
    print(f'Não, {a}, {b} e {c} não formam um triângulo.')