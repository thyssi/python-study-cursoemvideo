# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

over18 = mencount = underwomen = 0

while True:
    title = ' CADASTRO '
    print(f'{title:=^40}')
    nome = str(input('Nome: '))

    #idade
    while True:
        idade = int(input('Idade: '))
        if idade > 0:
            break

    #sexo
    while True:
        sexo = str(input('Sexo [F/M]: ')).strip().lower()[0]
        if sexo in 'fm':
            break

    #continuar, validação input
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar in 'sn':
            break

    #att contadores
    if idade >= 18:
        over18 += 1
    if sexo == 'm':
        mencount += 1
    if sexo == 'f' and idade < 20:
        underwomen += 1

    #continuar
    if continuar == 'n':
        break

print('='*40, f'''\nRELATÓRIO FINAL
{over18} pessoas maiores de idade
{mencount} homens cadastrados
{underwomen} mulheres sub-20''')