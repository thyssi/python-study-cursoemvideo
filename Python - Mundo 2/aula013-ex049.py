# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

fator1 = int(input('Escolha o fator: '))
title = ' TABUADA '
print(f'{title:=^20}')
for fator2 in range (0, 21):
    conta = f'{fator1:>3} x {fator2:>3} = {fator1*fator2:>3}'
    print(f'{conta:^20}')