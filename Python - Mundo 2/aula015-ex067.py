# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:

    # Loop quebra em número negativo
    fator1 = int(input('Escolha o número da tabuada: '))
    if fator1 < 0:
        break

    #Titulo
    title = f' TABUADA DO {fator1} '
    print(f'\033[33m{title:=^30}\033[m')

    #Loop da operação
    for fator2 in range (1, 11):
        conta = f'{fator1:>3} x {fator2:>3} = {fator1*fator2:>3}'
        print(f'\033[33m{conta:^30}\033[m')

    #Linha final
    print('\033[33m=\033[m'*30)

print('\033[30;107mPrograma Encerrado\033[m') #Encerramento cod