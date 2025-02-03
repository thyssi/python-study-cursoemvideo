# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha():
    p = input('Nome do jogador: ').capitalize().strip()
    g = input('Quantidade de gols: ')
    if p == '':
        p = '<desconhecido>'
    if g == '':
        g = 0
    print('-'*20)
    print(f'Jogador(a) {p} fez {g} gol(s).')

ficha()