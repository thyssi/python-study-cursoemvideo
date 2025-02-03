# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
# valor monetário formatado.

from CursoemVideo.modulos import moeda

num = float(input('Informe o valor do produto: '))

print(f'Aumento de 15% neste produto equivale a {moeda.moeda(moeda.aumentar(num, 15))}')
print(f'Desconto de 27% neste produto equivale a {moeda.moeda(moeda.diminuir(num, 27))}')
print(f'O dobro é {moeda.moeda(moeda.dobro(num))} e a metade é {moeda.moeda(moeda.metade(num))}')