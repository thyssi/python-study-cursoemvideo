# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def fatorial (n=0, show=False):

    print(f'Fatorial de {n} (com cálculo):') if show else print(f'Fatorial de {n}: ', end='')

    r = 1
    while n != 1:
        if show:
            print(n, end=' x ')
        r *= n
        n -= 1

    if show:
        print('1 =', r)
    else:
        print(r)

fatorial(7, True)