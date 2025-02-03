# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas
# b) a média de idade do grupo
# c) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da média

lista, user, soma, mulheres, over = list(), dict(), 0, list(), list()
while True:
    user['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        user['sexo'] = str(input('Sexo: ')).strip().lower()
        if user['sexo'][0] in 'fm':
            break
    if user['sexo'] == ' f':
        mulheres.append(user['nome'])
    while True:
        user['idade']  = int(input('Idade: '))
        if user['idade'] >= 0:
            break
    soma += user['idade']
    lista.append(user.copy())
    user.clear()
    while True:
        continuar = str(input('Continuar cadastro? [S/N] ')).strip().lower()
        if continuar[0] in 'sn':
            break
    if continuar[0] == 'n':
        break

for c in lista:
    if c['idade'] > soma/len(lista):
        over.append(c['nome'])

print(f'''
Foram cadastradas {len(lista)} pessoas.
A média de idade do grupo é {soma/len(lista):.1f}.
As mulheres do grupo são {mulheres}
As pessoas que tem a idade acima da média são {over}''')