# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# a) qual é o total gasto na compra
# b) quantos produtos custam mais de R$1000,00
# c) qual é o nome do produto mais barato

# Cabeçalho
loja = ' MERCADINHO FAROFA '
print('='*40)
print(f'{loja:^40}')
print('='*40)

cont = total = over1000 = barato_preco = 0
barato_nome = ''

while True:
    cont += 1
    print(f'Produto #{cont}')
    produto = str(input('Nome: ')).strip().title()
    preco = float(input('Preço: R$ '))
    total += preco

    if preco > 1000:
        over1000 += 1

    if barato_preco == 0 or preco < barato_preco:
        barato_preco = preco
        barato_nome = produto
    #elif preço < barato_preço:
        #barato_preço = preço

    continuar = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
    print('-' * 40)
    if continuar == 'n':
        break

linha_total = f' TOTAL: R$ {total:.2f}'
linha_over = f' ACIMA DE 1000: {over1000}'
linha_barato = f' PRODUTO MAIS BARATO: {barato_nome}'
print(f'{linha_total:.>40}\n{linha_over:.>40}\n{linha_barato:.>40}')