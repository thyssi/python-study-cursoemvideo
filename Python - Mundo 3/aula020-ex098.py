# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
# contagem. Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador (i, f, p):

    if p < 0:
        p *= -1
    if p == 0:
        print('Contagem não é possível.')

    print('-'*40)
    print(f'\033[35mContagem de {i} a {f}, a cada {p}:\033[m')

    if i < f:
        while i <= f:
            print(i, end=' ')
            sleep(.5)
            i += p
        print()
    elif i > f:
        while i >= f:
            print(i, end=' ')
            sleep(.5)
            i -= p
        print()
    else:
        print('Contagem não é possível.')

contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input(f'Início: ')), int(input('Fim: ')), int(input('Passo: ')))