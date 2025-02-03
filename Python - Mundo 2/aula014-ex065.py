# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

qnt_num, soma_num, maior_num, menor_num, continuar = 0, 0, 0, 0, 's'

while continuar == 's':
    num = int(input('Digite um número: '))

    qnt_num += 1 #Contador
    soma_num += num #Acumulador

    if menor_num == 0 or num < menor_num:
        menor_num = num #Menor
    elif num > maior_num:
        maior_num = num #Maior

    continuar = str(input('Você quer continuar? [S/N] ')).lower().strip()

    if 'n' != continuar != 's': #Erro
        continuar = str(input('\033[31mOpção inválida. Digite novamente [S/N]: \033[m'))

print(f'\n\033[36mQuantos: {qnt_num}\nMédia: {soma_num/qnt_num}\nMaior: {maior_num}\nMenor: {menor_num}\033[m')