# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.

lista, lista_par, lista_impar = list(), list(), list()

while True:
    lista.append(int(input('Digite um número: ')))

    #continuar
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
        if continuar in 'sn':
            break
    if continuar == 'n':
        break

for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)

print(f'''Lista normal: \033[33m {lista}\033[m
Lista par: \033[33m {lista_par}\033[m
Lista impar: \033[33m {lista_impar}\033[m''')

