# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável. Ex: escreva('Olá, Mundo!')
# Saída: ~~~~~~~~~~~
#        Olá, Mundo!
#        ~~~~~~~~~~~

def escreva(tex):
    l = len(tex)
    print('~'*l)
    print(tex)
    print('~' * l)

escreva(str(input('Escreva uma frase qualquer: ')))