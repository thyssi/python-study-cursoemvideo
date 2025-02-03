# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valor_inicial = float(input('Me informe o valor do item: R$ '))
print('''Formas de pagamento: 
                1. à vista em dinheiro ou cheque
                2. à vista no cartão
                3. em até 2x no cartão
                4. 3x 'ou mais no cartão''')
meio = int(input('Informe o número da forma de pagamento desejada: '))

if meio == 1:
    valor_final = valor_inicial*((100-10)/100)
elif meio == 2:
    valor_final = valor_inicial*((100-5)/100)
elif meio == 3:
    valor_final = valor_inicial
else:
    valor_final = valor_inicial*(1+(20/100))

print(f'O valor que você vai pagar pelo produto, considerando descontos ou juros, é de R$ \033[40;1m{valor_final:.2f}\033[m')
