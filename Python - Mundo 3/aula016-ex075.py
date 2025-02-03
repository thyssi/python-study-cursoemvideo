# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9:
# b) em que posição foi digitado o primeiro valor 3:
# c) quais foram os números pares.

tupla = par = ()

for c in range (0, 4):
    num = int(input('Digite um número: '))
    tupla += (num,)
    if num % 2 == 0:
        par += (num,)

print(f'O valor 9 apareceu {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O valor 3 apareceu pela 1° vez na {tupla.index(3)+1}° posição')
else:
    print(f'Não há valor 3.')

print('Não há nenhum número par.') if par == () else print( f'Os números pa res são {par}')