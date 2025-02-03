# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
# já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista_num = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista_num:
        lista_num.append(num)

    while True: #rep caso resp n seja s ou n
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()
        if continuar in 'sn':
            break
    if continuar == 'n':
        break

print(f'Os números inseridos são:', sorted(lista_num))
