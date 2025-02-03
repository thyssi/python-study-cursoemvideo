# Refaça o DESAFIO 035 dos triãngulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = float(input('Informe a medida da 1° reta: '))
b = float(input('Da 2°: '))
c = float(input('Da 3°: '))

if (b-a) < c < (b+a) and (a-c) < b < (a+c) and (c-b) < a < (c+b):
    print(f'Sim, {a}, {b} e {c} formam um triângulo.')
    if a == b == c:
        print('E este triângulo é equilátero.')
    elif a != b != c != a:
        print('E este triângulo é escaleno.')
    else:
        print('E este triângulo é isósceles.')
else:
    print(f'Não, {a}, {b} e {c} não formam um triângulo.')