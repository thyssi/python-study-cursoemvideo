# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

start = 0
for c in range (0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        start += num
print(f'\033[35;1mA soma dos seis números é {start}\033[m')