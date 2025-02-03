# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.

tipo = int(input('Digite 0 para pares e 1 para ímpares: '))
mult = int(input('Digite a base de multiplicação: '))
start = 0
soma = 0
for c in range (0, 500):
    start += 1
    if start % mult == 0 and start % 2 == tipo:
        # print(start, end=' ') # Lista dos números que atendem a condição if
        soma += start
print(f'\033[34mNo intervalo de 1 até 500, a soma dos números {'ímpares' if tipo == 1 else 'pares'} e múltiplos de {mult} é \033[97;44;1m{soma}\033[m')
