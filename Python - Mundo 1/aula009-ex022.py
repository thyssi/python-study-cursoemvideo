# Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas e minúsculas.
#   - Quantas letras ao todo (sem considerar espaços).
#   - Quantas letras tem o primeiro nome.

fullname = input('Insira o nome completo aqui: ').strip()
print(f'Nome em maiúsculo: {fullname.upper()}')
print(f'Nome em minúsculo: {fullname.lower()}')
fullname_splited = fullname.split()
fullname_jointed = ''.join(fullname_splited)
print(f'Total de letras nome completo: {len(fullname_jointed)}')
print(f'Total de letras 1° nome: {len(fullname_splited[0])}')