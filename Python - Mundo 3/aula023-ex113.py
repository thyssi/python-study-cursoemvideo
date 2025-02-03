# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de 
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(frase):

    try:
        global n
        while True:
            n = input(frase)

            #validação negativos e decimais
            #    um caractere
            if len(n) == 1 and n in '1234567890':
                inteiro = True
            elif len(n) == 1 and n not in '1234567890':
                inteiro = False
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            #    +1 caractere
            elif n[0] in '-1234567890':
                for c in n[1:]:
                    if c not in '1234567890':
                        inteiro = False
                        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                        break
                    inteiro = True
            elif n[0] not in '-1234567890':
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                inteiro = False
            else:
                inteiro = True

            if inteiro:
                break
    except IndexError:
        print('Insira um valor válido.')

print('-'*20)
leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')