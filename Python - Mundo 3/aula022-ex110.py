# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

from CursoemVideo.modulos import moeda

valor = float(input('Qual o valor? '))
moeda.resumo(valor, 25, 15)