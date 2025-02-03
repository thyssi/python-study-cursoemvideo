# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - a média de idade do grupo;
# - qual é o nome do homem mais velho;
# - quantas mulheres têm menos de 20 anos.

soma_idade = 0
idade_max = 0
nome_homem = ''
qnt_mulher = 0

for c in range (0, 4):
    nome = str(input('Informe seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('E seu sexo (F ou M): ')).strip().lower()

    # Média de idade
    soma_idade += idade

    # Nome do homem mais velho
    if sexo == 'm' and idade > idade_max:
        nome_homem = nome
        idade_max = idade

    # Quantas mulheres tem menos de 20 anos
    if sexo == 'f' and idade < 20:
        qnt_mulher += 1

print(f'''A média de idade do grupo é de {soma_idade/4} anos.
O homem mais velho é o {nome_homem}, com {idade_max} anos.
No total {qnt_mulher} mulher(es) tem menos de 20 anos.''')