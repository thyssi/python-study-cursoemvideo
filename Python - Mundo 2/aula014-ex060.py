# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5!=5x4x3x2x1=120

num = int(input('Insira um número inteiro qualquer: '))
num_fat = num
multi = 1

print(f'''Fatorial:
{num_fat}! = ''', end='') # fatorial x!
while num != 1:
    print(f'{num}', end=' x ')
    multi *= num
    num -= 1
print(f'1 = {multi}') # último fator 1