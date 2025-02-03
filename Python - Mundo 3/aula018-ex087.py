# Aprimore o desafio anterior, mostrando no final:
# a) a soma de todos os valores pares digitados
# b) a soma dos valores da terceira coluna
# c) o maior valor da segunda linha

matriz = [[],[],[]]
soma_par = soma_tudo = 0
for c in range (0, 3):
    for a in range (0, 3):
        matriz[c].append(int(input(f'Número {c}x{a}: ')))

print('')
for c in range (0, 3):
    for a in range (0, 3):
        print(f'[{matriz[c][a]:^5}]', end='')
        soma_tudo += matriz[c][a]
        if matriz[c][a] % 2 == 0:
            soma_par += matriz[c][a]
    print('')

print(f'''
Todos os valores somados: {soma_tudo}
Todos os valores pares somados: {soma_par}
Soma dos valores da 3° coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}
Maior valor da 2° linha: {max(matriz[1])}''')
