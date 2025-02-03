# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa que você quer financiar? R$ '))
salario = float(input('Qual o seu salário atual? R$ '))
tempo_financiamento = int(input('Em quantos anos você pretende financiar? '))*12
prestacao_user = salario*(30/100)
prestacao_real = valor_casa/tempo_financiamento
if prestacao_user >= prestacao_real:
    print(f'Parabéns, o seu financiamento foi \033[97;46;4maprovado\033[m! As suas parcelas serão de R$ {prestacao_real:.2f},', end=' ')
    print(f'a serem pagas em {tempo_financiamento} meses ({int(tempo_financiamento/12)} anos).')
else:
    print('Ahhh, que pena! O seu financiamento \033[97;41;1mnão foi aprovado\033[m! Com o seu salário atual e o tempo de financiamento pretendido,')
    print(f'o seu imóvel precisaria ter o valor total máximo de R$ {(prestacao_user*tempo_financiamento):.2f}')
print('Espero ter esclarecido as suas dúvidas!')