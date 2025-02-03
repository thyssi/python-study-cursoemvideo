# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = ()

for c in range (0, 5):
    x = randint(0,10)
    tupla += (x,)

print(f'Os números gerados foram {tupla}\nO menor número é {sorted(tupla)[0]} e o maior é {sorted(tupla)[4]}')