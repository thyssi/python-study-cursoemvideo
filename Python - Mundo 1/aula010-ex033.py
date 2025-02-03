# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
a = [n1, n2, n3]
list.sort(a)

print(f'O maior número é {a[2]} e o menor é {a[0]}')