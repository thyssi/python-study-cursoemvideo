# Crie um programa onde o usuário digite uma expressão qualquer que use parêntesis. Seu aplicativo deverá analisar se
# a expressão passada está com os parêntesis abertos e fechados na ordem correta.

frase = input('Digite a expressão: ').replace(' ', '')
lista, ordem = list(), ''

# extrair ()
for c in frase:
    if c in '()':
        lista.append(c)

if lista.count('(') == lista.count(')'): #( e ) tem que ter msm quantidade
    if lista[0] == ')' or lista[-1] == '(': #precisa começar com ( e terminar com )
        ordem = 'incorreta'
    else:
        ordem = 'correta'
else:
    ordem = 'incorreta'

print(f'A ordem está {ordem}.')