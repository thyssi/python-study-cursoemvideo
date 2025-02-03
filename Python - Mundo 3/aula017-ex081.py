# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) quantos números foram digitados
# b) a lista de valores ordenada de forma decrescente.
# c) se o valor 5 foi digitado e está ou não na lista

lista = list()

while True:
    lista.append(int(input('Digite um número: ')))

    while True: #rep se typo
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
        if continuar in 'sn':
            break

    if continuar == 'n': #saida
        break

print(f'''Foram digitados {len(lista)} números.
A lista decrescente é:\n{sorted(lista, reverse=True)}
O número 5 {'foi encontrado' if 5 in lista else 'não foi encontrado'} na lista!''')

