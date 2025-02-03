# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas funções.

from CursoemVideo.modulos import moeda

num = float(input('Informe o valor do produto: '))

print(f'Aumento de 15% neste produto equivale a {moeda.aumentar(num, 15)}')
print(f'Desconto de 27% neste produto equivale a {moeda.diminuir(num, 27)}')
print(f'O dobro é {moeda.dobro(num)} e a metade é {moeda.metade(num)}')