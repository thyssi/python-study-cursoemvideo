# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Qual o ano analisado? '))

if ano % 100 == 0:
    if ano % 400 == 0:
        print('É bissexto.')
    else:
        print('Não é bissexto.')
else:
    if ano % 4 == 0:
        print('É bissexto.')
    else:
        print('Não é bissexto.')