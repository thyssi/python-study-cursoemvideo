# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

def leiaint(frase):
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

print('-'*20)
leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')