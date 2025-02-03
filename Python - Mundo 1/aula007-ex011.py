# Faça um programa que leia a largura e a altura de uma parede em m, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
l = float(input('Largura: '))
a = float(input('Altura: '))
m2p = l*a
t = m2p/2
print(f'Área quadrada: {m2p:.2f} m² \nTinta necessária: {t:.2f} L')