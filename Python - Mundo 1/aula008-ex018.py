# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
graus = float(input('Insira um ângulo aqui (°): '))
radianos = math.radians(graus)
print(f'O cosseno de {graus}° é {(math.cos(radianos)):.3f}, \nseu seno é {(math.sin(radianos)):.3f} \ne o tangente é {(math.tan(radianos)):.3f}')
