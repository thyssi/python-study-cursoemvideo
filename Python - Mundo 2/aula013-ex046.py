# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até
# 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

input('Aperte enter para começar a contagem regressiva. ')
print('\033[33;1mIniciando a contagem regressiva de 10 segundos...\033[m')
n = 1
start = 10
for c in range (0, 10):
    sleep(1)
    start -= n
    print(f'{start+1}...')
sleep(1)
print(emoji.emojize(':fireworks:'*10))

