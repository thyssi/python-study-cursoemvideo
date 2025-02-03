from time import sleep
def contador (i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        sleep(.4)
        c += p
    print('FIM!')

contador(0, 100, 10)
help(contador)