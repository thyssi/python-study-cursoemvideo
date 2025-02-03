# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
# simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from CursoemVideo.modulos.alpha import *
from CursoemVideo.modulos.ext import *

arq = 'cursoemvideo.txt'

if arquivoexiste(arq):
    print('Arquivo encontrado.')
else:
    print('Arquivo não encontrado.')
    criararquivo(arq)

while True:
    l = 40
    linha_separacao(l)
    titulo('menu principal', l)
    linha_separacao(l)
    opcao(1, 'Ver pessoas cadastradas')
    opcao(2, 'Cadastrar nova pessoa')
    opcao(3, 'Sair do Sistema')
    linha_separacao(l)
    try:
        user = int(input('Sua opção: '))
    except ValueError:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    else:
        if  user == 1:
            ver_dados(l)
        elif user == 2:
            nome = str(input('Nome: ')).strip().title()
            idade = int(input('Idade: '))
            cadastrar_dados(nome, idade)
        elif user == 3:
            break
        else:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
titulo('fim', l)



