# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

info = {'nome':str(input('Nome: ')).capitalize().strip(),
        'idade':date.today().year - int(input('Ano de nascimento: ')),
        'ctps':int(input('No. CTPS (0 se n houver): '))}
if info['ctps'] != 0:
    info['admissao'] = int(input('Ano de contratação: '))
    info['salario'] = float(input('Salário: R$ '))
    info['aposentadoria'] = info['admissao']+35-date.today().year+info['idade']

print(info)

print(f'{info['nome']} se aposentará com {info['aposentadoria']} anos.')