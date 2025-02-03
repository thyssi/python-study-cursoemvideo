# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qnt_termo = 0

print('Os 10 primeiros termos dessa PA são: ')

while qnt_termo != 10:
    print(termo+razao, end=' ')
    termo += razao
    qnt_termo += 1

qnt_mais = 1

while qnt_mais != 0:

    qnt_mais = int(input('\nVocê quer ver mais alguns termos? Quantos? Preencha 0 caso nenhum. '))
    qnt_termo = 0
    cnt_mais = 0

    while qnt_termo != qnt_mais:
        print(termo+razao, end=' ')
        termo += razao
        qnt_termo += 1

print('FIM')