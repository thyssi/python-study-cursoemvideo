# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
divisor = num
tipo = 'É primo'
for c in range (1, num-1):
    divisor -= 1
    if num % divisor == 0:
        tipo = 'Não é primo'
print(f'\033[32m{tipo}')
