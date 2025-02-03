# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
for c in range (0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Valores pares: {sorted(lista[0])}\nValores ímpares: {sorted(lista[1])}')