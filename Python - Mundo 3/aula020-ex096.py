# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(l, p):
    a = l * p
    print('=' * 25)
    print(f'{'Cálculo de Terreno':^25}')
    print('=' * 25)
    print(f'Largura (m): {l}m\nProfundidade (m): {p}m\nA área do terreno é {a:.2f}m²')

area(float(input('Informe a largura do terreno: ')), float(input('Informe a profundidade do terreno: ')))
area(5, 25)
area(10, 30)