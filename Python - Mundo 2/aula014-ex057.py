# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input('Informe o sexo [F/M]: ')).strip().lower()[0]

while 'f' != sexo != 'm': #alternativa while sexo not in 'mf':
    sexo = str(input('Opção inválida. Tente novamente: '))

if sexo == 'f':
    print(f'Entendi, você é do sexo \033[31;4mfeminino\033[m.')
else:
    print(f'Entendi, você é do sexo \033[34;4mmasculino\033[m.')

