# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido.

from random import choice
a1, a2, a3, a4 = input('Aluno 1: '), input('Aluno 2: '), input('Aluno 3: '), input('Aluno 4: ')
print(f'O responsável da vez é o(a) {choice ([f'{a1}', f'{a2}', f'{a3}', f'{a4}'])}')
