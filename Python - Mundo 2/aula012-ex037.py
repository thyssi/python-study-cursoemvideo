# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número: '))
base_user = int(input('Escolha a base de conversão (1 binário, 2 octal, 3 hexadecimal): '))
if base_user == 1:
    num_conv = f'{num:b}'
elif base_user == 2:
    num_conv = f'{num:o}'
elif base_user == 3:
    num_conv = f'{num:x}'
else:
    print('Opção inválida.')

if 0 <= base_user <= 3:
    print(f'De acordo com a base de conversão escolhida, o número convertido equivale a \033[44;4m{num_conv}\033[m')