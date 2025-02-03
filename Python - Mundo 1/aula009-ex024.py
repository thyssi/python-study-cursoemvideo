# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Insira uma cidade: ').strip()
cidade_min = (cidade.lower()).split()
print(f'A cidade selecionada começa com "Santo": {'santo' in cidade_min[0]}')
