lanche = ('Burger', 'Suco', 'Pizza', 'Pudim')

#não precisa de posição
for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-' * 10)

#se precisar da posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-'*10)

#se precisar da posição + dado
for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posiçao {pos}')

print('-'*10)

print('Comi pakas')