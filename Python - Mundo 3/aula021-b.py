def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: 1° valor
    :param b: 2° valor
    :param c: 3° valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(5, 7) 
somar(c=9, a=1)
somar()
help(somar)