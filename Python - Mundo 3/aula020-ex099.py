# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(x):
    mai = max(lista)
    print('-' * 20)
    print(f'Os números informados são {lista}.\nO maior número é {mai}')
    print('-' * 20)


lista = []
while True:
    lista.append(int(input('Insira os valores: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N} ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar == 'n':
        break

maior(lista)