# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.

banco = 'BANCO DO PYTHON'
print('='*40)
print(f'{banco:^40}')
print('='*40)

valor = float(input('Quanto você quer sacar? R$ '))
nota50 = nota20 = nota10 = nota1 = 0

nota50 = valor // 50
resto = valor % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota1 = resto // 1
resto = resto % 1

print(f'Você vai sacar:\n{int(nota50)} notas de R$50\n{int(nota20)} notas de R$20\n{int(nota10)} notas de R$10\n{int(nota1)} notas de R$1\nvão sobrar {resto} centavos na sua conta.')
print('='*40)