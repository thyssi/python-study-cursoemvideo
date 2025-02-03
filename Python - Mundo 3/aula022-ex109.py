# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from CursoemVideo.modulos import moeda

num = float(input('Informe o valor do produto: '))

print(f'Aumento de 30% neste produto equivale a {moeda.aumentar(num, 30, real=False)}')
print(f'Desconto de 55% neste produto equivale a {moeda.diminuir(num, 55, real=True)}')
print(f'O dobro é {moeda.dobro(num, real=True)} e a metade é {moeda.metade(num, real=True)}')