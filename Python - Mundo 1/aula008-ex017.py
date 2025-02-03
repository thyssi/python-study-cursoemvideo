# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o
# comprimento da hipotenusa.

from math import sqrt, pow, hypot

co, ca = float(input('Medida do cateto oposto: ')), float(input('Medida do cateto adjacente: '))
print(f'A medida da hipotenusa é {sqrt(pow(co,2)+(pow(ca, 2)))}')
print(f'É {hypot(co, ca)}')