# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona

frase = str(input('Insira a sua frase aqui: '))
frase = frase.strip().lower().replace(' ', '')
carac_L = len(frase)
carac_R = -1

tipo = 'É palindromo.'

for c in range (0, len(frase)):
    carac_R += 1
    carac_L -= 1
    if frase[carac_R] != frase[carac_L]:
        tipo = 'Não é palindromo.'

print(tipo)