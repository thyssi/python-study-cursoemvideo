# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = float(input('Escolha um número: '))
num2 = float(input('Escolha outro número: '))

if num1 < num2:
    print(f'O SEGUNDO número é maior do que o PRIMEIRO.')
elif num1 > num2:
    print(f'O PRIMEIRO número é maior do que o SEGUNDO.')
else:
    print(f'Não existe valor maior, AMBOS são iguais.')