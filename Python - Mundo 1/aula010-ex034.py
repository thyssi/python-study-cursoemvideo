# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, e calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o seu salário? '))

if sal > 1250:
    aumento = 10
else:
    aumento = 15

sal_novo = sal*((100+aumento)/100)

print(f'Seu novo salário  é R$ {sal_novo:.2f}')