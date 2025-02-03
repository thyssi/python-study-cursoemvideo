# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#   Ex: digite um número: 1827 ==> un: 7 dez: 2 cen: 2 mil: 1

num = int(input('Insira um número inteiro de 0 a 9999: '))
num_4digit = (f'{num:0>4}')
num_mil, num_cen, num_dez, num_un = num_4digit[0], num_4digit[1], num_4digit[2], num_4digit[3]
print(f'Valor unidade: {num_un}, valor dezena: {num_dez}, valor centena: {num_cen}, valor milhar: {num_mil}')
