# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num_user = int(input('Qual o número analisado? '))
rest = num_user%2
if rest == 0:
    print('O seu número é par.')
else:
    print('O seu número é ímpar.')