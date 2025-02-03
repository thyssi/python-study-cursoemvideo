# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

user, data = list(), list()
while True:
    user.append(str(input('Nome: ')))
    user.append(float(input('Nota 1: ')))
    user.append(float(input('Nota 2: ')))
    data.append(user[:])
    user.clear()
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).strip().lower()
        if continuar[0] in 'sn':
            break
    if continuar[0] in 'n':
        break

print('='*20)
print(f'{'BOLETIM DE NOTAS':^20}')
print('='*20)

for i, c in enumerate(data):
    print(f'#{i+1}\nNome: {c[0].capitalize()}\nMédia: {(c[1]+c[2])/2:.2f}\n{'-'*20}')

while True:
    while True:
        individual = int(input('Digite o número de chamada para ver as notas individuais (999 encerra): '))
        if individual == 999 or individual <= len(data):
            break
    if individual == 999:
        break
    else:
        individual -= 1
        print('-'*20)
        print(f'#{individual+1}\nNome: {data[individual][0]}\nNota 1: {data[individual][1]}\nNota 2: {data[individual][2]}')
        print('-' * 20)
print('FIM')