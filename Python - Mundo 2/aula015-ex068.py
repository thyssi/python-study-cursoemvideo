# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

wincount = 0

while True:
    pc = randint(0, 1)
    user = int(input('Escolha um número: '))
    guess = int(input('Par ou ímpar? [0/1] '))
    guess = 'par' if guess == 0 else 'ímpar'
    resultado = 'par' if (pc+user) % 2 == 0 else 'ímpar'

    if guess == resultado:
        wincount += 1
        print(f'Número PC: {pc}  Seu número: {user}  Seu Chute: {guess} Resultado: \033[36m{resultado}\033[m\n')
    else:
        print(f'Número PC: {pc}  Seu número: {user}  Seu Chute: {guess} Resultado: \033[36m{resultado}\033[m\n')
        break

print(f'Total de vitórias consecutivas: {wincount}\nParabéns!')
