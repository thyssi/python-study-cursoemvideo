# Faça um programa que tenha ums lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.

from random import randint

numeros = []
def sorteia (x):
    while len(numeros) != x:
        num = randint(1, 10)
        if num not in numeros:
            numeros.append(num)
    print(numeros)

def somapar (x):
    soma = 0
    for c in x:
        if c % 2 == 0:
            soma += c
    print(soma)

sorteia(5)
somapar(numeros)

# 20/01/2025