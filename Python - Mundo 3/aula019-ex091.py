# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
s = 0
game = list()
sleep(s)
for c in range (1, 5):
    print(f'Jogador {c} está jogando o dado...')
    sleep(s)
    dado = randint(1, 6)
    print(f'\033[36m{dado}\033[m')
    sleep(s)
    play = {'jogador': c, 'dado': dado}
    game.append(play)

print(game)