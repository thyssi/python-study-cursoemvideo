# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
from datetime import date
ano_nasc = int(input('Informe o ano de nascimento: '))
ano_hoje = date.today().year
idade = ano_hoje-ano_nasc
if idade <= 9:
    categ = 'MIRIM'
elif idade <= 14:
    categ = 'INFANTIL'
elif idade <= 19:
    categ = 'JUNIOR'
elif idade <= 25:
    categ = 'SENIOR'
else:
    categ = 'MASTER'
print(f'Você tem {idade} anos, e a sua categoria é {categ}! Boa sorte na competição!')