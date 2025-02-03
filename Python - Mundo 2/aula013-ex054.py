# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import datetime

menor = 0
maior = 0

for c in range (0, 7):
    ano = int(input('Insira o ano de nascimento: '))
    if datetime.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'\033[97;45;1m{maior}\033[m pessoas já atingiram a maioridade e \033[97;45;1m{menor}\033[m pessoas ainda não.')