# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente. Ex: Ana Maria de Souza Primeiro: Ana Último: Souza

nome = input ('Nome completo: ').strip()
n_striped = (nome.strip()).title()
n_splited = n_striped.split()
print(f'Seu primeiro nome é {n_splited[0]} e o último é {n_splited[len(n_splited) - 1]}.')