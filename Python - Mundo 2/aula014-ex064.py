# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

soma_num = 0    #O código soma o 999
qnt_num = 0        #O código conta o 999
num = 0

num = int(input('Digite um número inteiro: '))
while num != 999:
    soma_num += num
    qnt_num += 1
    num = int(input('Digite um número inteiro: '))

print(soma_num)
print(f'Foram digitados {qnt_num} números e a soma deles é {soma_num}')