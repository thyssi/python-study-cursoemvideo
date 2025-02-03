# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves

dados, user, pesos = list(), list(), list()

while True:
    dados.append(str(input('Informe o nome: ')).strip().title())
    dados.append(float(input('Informe o peso: ')))
    user.append(dados[:])
    dados.clear()
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).strip().lower()
        if continuar[0] in 'sn':
            break
    if continuar[0] == 'n':
        break
print(f'Foram cadastradas {len(user)} pessoas.')

for v in user: #criar lista só de pesos
    pesos.append(v[1])
pesomai, pesomen = max(pesos), min(pesos)

print('Pessoas mais pesadas: ', end='')
for v in user:
    if v[1] == pesomai:
        print(f'{v[0]} co m {v[1]}KG...', end=' ')

print('\nPessoas mais leves: ', end='')
for v in user:
    if v[1] == pesomen:
        print(f'{v[0]} com {v[1]}KG...', end=' ')