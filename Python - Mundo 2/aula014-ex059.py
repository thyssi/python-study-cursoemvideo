# Crie um programa que leia dois valores e mostre um menu na tela: 1. Somar 2. Multiplicar 3. Maior 4. Novos Números
# 5. Sair do Programa // Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

# Enquanto não cinco, loopa.
while opcao !=5:
    print('============ MENU =============')
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    # Menu
    print(f'''\033[34mSeus números são {n1} e {n2}.
    O que você quer fazer com eles?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] ESCOLHER NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA\033[m''')
    opcao = int(input('Operação escolhida: '))

    # Operações 1 ao 3
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        print(f'O maior número é {n1 if n1 > n2 else n2}')

    # Opção de retorno só do 1 ao 3, 4 volta direto
    if opcao != 4:
        retorno = str(input('Voltar ao menu? [S/N] ')).strip().lower()
        if retorno == 'n': # Opção = 5 sai do while
            opcao = 5

print('FIM')