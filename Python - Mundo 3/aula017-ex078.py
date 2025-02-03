# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

#lista
lista = list()
for c in range (0,5):
    lista.append(int(input('Digite um valor numérico: ')))

#print da lista
print('Os números da lista são:', end=' ')
for i in lista:
    print(i, end=' ')

maxi, mini = max(lista), min(lista)

print(f'\nO maior número digitado foi {maxi}, ', end='')

#maior
if lista.count(maxi) > 1:
    print('nas posições ', end='')
    for i, v in enumerate(lista):
        if v == maxi:
            print(f'{i}...', end=' ')
else:
    print(f'na posição {lista.index(maxi)}.', end='')

print(f'\nO menor número digitado foi {mini}, ', end='')

#menor
if lista.count(mini) > 1:
    print('nas posições ', end='')
    for i, v in enumerate(lista):
        if v == mini:
            print(f'{i}...', end=' ')
else:
    print(f'na posição {lista.index(mini)}.')