# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

n = int(input('Quantos jogos você quer? '))
jogo, apostas = [], []

for c in range (0, n):
    sleep(1)
    for a in range (0, 6):
        while len(jogo) != 6:
            bola = randint(1, 60)
            if bola not in jogo:
                jogo.append(bola)
    print(f'\nGerando jogo #{c+1}...')
    sleep(1)
    for b in sorted(jogo):
        print(b, end=' ')
    apostas.append(sorted(jogo[:]))
    jogo.clear()
sleep(1)
print('\n', apostas)