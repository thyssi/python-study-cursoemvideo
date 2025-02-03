# Faça um algoritmo que mostre um preço de um produto e mostre seu novo preço, com 5% de desconto.
v1 = float(input('Insira o preço: R$ '))
d = v1*(5/100)
v2 = v1-d

print(f'Desconto (5%): -R${d:.2f}\nValor final: R$ {v2:.2f}')