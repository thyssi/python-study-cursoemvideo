# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
v1 = float(input('Salário atual: R$ '))
a = v1*0.15
v2 = v1+a
print(f'Aumento (15%): R$ {a:.2f}\nSalário ajustado: R$ {v2:.2f}')