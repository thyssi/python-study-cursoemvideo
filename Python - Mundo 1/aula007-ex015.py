# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

d = float(input('Quantos dias? '))
km = float(input('Quantos km percorridos? '))
print(f'O valor a ser pago de aluguel é R${((d*60)+(km*.15)):.2f}. A cotação atual é R$60,00/dia e R$0.15/km.')