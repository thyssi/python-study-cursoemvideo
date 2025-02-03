# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO, nas eleições.
def voto(nasc):
    from datetime import date
    if nasc < 0 or nasc > date.today().year:
        print('Ano Inválido')
    else:
        idade = date.today().year - nasc
        if 16 <= idade < 18 or idade >= 70:
            stt = 'OPCIONAL'
        elif idade < 16:
            stt = 'NEGADO'
        else:
            stt = 'OBRIGATÓRIO'
        print(f'Com {idade} anos: VOTO {stt}')

def linha(n):
    print('-'*n)

linha(25)
voto(int(input('Em que ano você nasceu? ')))