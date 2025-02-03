# Escreva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input ('Nota 1° bimestre: '))
n2 = float(input ('Nota 2° bimestre: '))
n3 = float(input ('Nota 3° bimestre: '))
m = (n1+n2+n3)/3
n4 = 24-(n1+n2+n3)
print(f'A sua média atual é {m:.2f}', end ='. ')
print(f'Você precisa tirar {n4:.2f} no 4° bimestre para passar de ano.')