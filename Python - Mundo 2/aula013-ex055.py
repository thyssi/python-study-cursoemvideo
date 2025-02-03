# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range (0, 5):
    peso =  float(input('Informe o peso: '))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso informado é {maior:.2f} kg e o menor é {menor:.2f} kg.')