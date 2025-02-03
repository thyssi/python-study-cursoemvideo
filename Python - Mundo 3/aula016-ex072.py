# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user = int(input('Escolha um número de 0 a 20: '))
    if 0 <= user <= 20:
        break

print(f'Seu número por extenso é: {num[user]}')
