# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

tupla = ('batatinha', 'cabelo', 'aspirador', 'pedra', 'borboleta',
         'nuvem', 'ilha', 'spray', 'gelatina', 'celular', 'bruxa',
         'coleira', 'biquini', 'lençol', 'ovo', 'cadeira')

for c in range (0, len(tupla)): #repetir qnt de itens da tupla, c = cada vez
    print(f'Palavra: {tupla[c]}\nVogais: ', end='')
    for l in range (0, len(tupla[c])): #repetir qnt de letras do item
        if tupla[c][l] in 'aeiou':
            print(tupla[c][l], end=' ')
    print('\n'+'-'*10)