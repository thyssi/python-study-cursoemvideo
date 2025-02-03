# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

num = randint(0,10)
guess = int(input('Tente adivinhar o número escolhido (vai de 0 a 10): '))
tentativas = 0

print('Conferindo a resposta...')
sleep(2)

while num != guess:
    guess = int(input('Booo! Errou, hehe! Tente de novo, vou te dar essa chance. '))
    # print('Dica: Um pouco mais...') if guess < num else print('Dica: Um pouco menos...')
    sleep(2)
    tentativas += 1

print(f'''Parabéns, você acertou usando {tentativas} tentativa(s)!
Obrigada pela brincadeira, vamos jogar de novo outro dia!''')