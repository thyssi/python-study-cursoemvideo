# Escreva um programa que leia um número X inteiro qualquer e mostre na tela os X primeiros elementos de uma
# sequência de fibonacci. Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

qnt_num = int(input('Digite um número: '))

while qnt_num == 0: #Erro
    qnt_num = int(input('\033[31mSequência inexistente.\033[m\nDigite um número: '))

num_1, num_2, num_3, cnt_num = 0, 1, 1, 0

print(f'Segue abaixo a sequência fibonacci:')
while cnt_num != qnt_num:
    if qnt_num == 1:
        print(num_1, end=' ')
        cnt_num = qnt_num
    elif qnt_num == 2:
        print(num_1, num_2, end=' ')
        cnt_num = qnt_num
    elif qnt_num >= 3:
        print(num_1, num_2, end=' ')
        cnt_num += 2
        while cnt_num != qnt_num:
            num_3 = num_1 + num_2
            print(num_3, end=' ')
            cnt_num += 1
            num_1 = num_2
            num_2 = num_3

print('\nFIM (aleluia, demorei demais, é importante dormir bem 05/01/2024)')
