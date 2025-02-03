def moeda(n):
    return f'R$ {float(n):8.2f}'.replace('.', ',')
def aumentar(n, per, real=False):
    f = n * (1+(per/100))
    return moeda(f) if real else f
def diminuir(n, per, real=False):
    f = n * (100-per)/100
    return moeda(f) if real else f
def dobro(n, real=False):
    f = n * 2
    return moeda(f) if real else f
def metade(n, real=False):
    f = n / 2
    return moeda(f) if real else f
def resumo(i, a, d, real=False):
    """
    i: valor
    a: % de aumento
    d: % de desconto
    real: formato monetário
    """
    def linha(n):
        print('='*n)
    def item(texto, valor, linha):
        print(f'{texto}{' '*(linha-len(texto)-len(valor))}{valor}')

    l = 45
    title = 'RESUMO DO VALOR'

    linha(l)
    print(f'{title:^{l}}')
    linha(l)
    item('Preço analisado:', moeda(i), l)
    item('Dobro do preço:', dobro(i, real=True), l)
    item('Metade do preço:', metade(i, real=True), l)
    item(f'{a}% de aumento:', aumentar(i, a, real=True), l)
    item(f'{d}% de desconto:', diminuir(i, d, real=True), l)
    linha(l)



