# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Batata Inglesa', 6, 'Cereal', 14, 'Arroz Arbóreo', 27, 'Morango', 11,
         'Salsicha', 4.5, 'Carne Moída', 22, 'Suco de Laranja', 17)

#cabeçalho
print('='*40)
print(f'{" FLYER DE PREÇOS ":^40}')
print('='*40)

#itens
for c in range(0, len(tupla), 2):
    item, preco = tupla[c] + ' ', f' R$ {(float(tupla[c+1])):.2f}'
    print(f'{item}{'.'*(40-len(item)-len(preco))}{preco}')
print('='*40)