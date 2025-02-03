# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
# o conteúdo da estrutura na tela.

user = {'nome': str(input('Nome: ')), 'média': float(input('Média: '))}
user['status'] = 'REPROVADO' if user['média'] < 7 else 'APROVADO'
print(f'O nome é {user['nome'].capitalize()}, média {user['média']:.2f} e seu status é {user['status']}.')