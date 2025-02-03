# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

fullname = input('Insira o seu nome completo: ').strip()
fullname_min = (fullname.lower()).split()
print(f'"Silva" faz parte do nome completo: {'silva' in fullname_min}')