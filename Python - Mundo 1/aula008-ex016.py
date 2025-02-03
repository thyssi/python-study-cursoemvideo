# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Escolha um número real: '))
print(f'Porção inteira deste número é {trunc(num)}')
print(f'É {int(num)}')