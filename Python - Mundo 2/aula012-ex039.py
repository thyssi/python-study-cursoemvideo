# Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu progresso também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from time import sleep

data_nasc = int(input('Em que ano você nasceu? '))
data_hoje = date.today().year
print('\033[43;0mProcessando... Aguarde um segundo...\033[m')
sleep(3)
if data_hoje-data_nasc == 18:
   print(f'Pelo que vi aqui, você está com {data_hoje-data_nasc} anos. Ou seja, chegou o ano do seu alistamento!')
elif data_hoje-data_nasc < 18:
   print(f'Você tem {data_hoje-data_nasc} anos. Ainda tem {18-(data_hoje-data_nasc)} ano(s) até o seu alistamento.')
else:
   print(f'Já se passaram {(data_hoje-data_nasc)-18} ano(s) desde a data do seu alistamento. Se apresente na sua JAM assim que possível.')
