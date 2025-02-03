# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu/perdeu.

from random import randint
from time import sleep
num = randint(0,5)
guess = input('Tente adivinhar o número escolhido (vai de 0 a 5): ').strip()
print('Conferindo a resposta...')
sleep(3)
if num == guess:
    print('Parabéns, você acertou!')
else:
    guess_2 = input('Booo! Errou, hehe! Tente de novo, você tem mais uma chance! ').strip()
    print('Conferindo a resposta...')
    sleep(3)
    if num == guess_2:
        print('Agora sim! Parabéns, você acertou!')
    else:
        print(f'Ahhh que pena, acabaram as suas chances! :c A resposta era {num}.')
print('Obrigada pela brincadeira, vamos jogar de novo outro dia!')