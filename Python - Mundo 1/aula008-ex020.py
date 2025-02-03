# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
# que leia o nome dos quatros alunos e mostre a ordem sorteada.
from random import shuffle

a1, a2, a3, a4 = input('Aluno 1: '), input('Aluno 2: '), input('Aluno 3: '), input('Aluno 4: ')
sorteio = [a1, a2, a3, a4]
shuffle(sorteio)
print(f'Ordem de apresentação é {sorteio}')