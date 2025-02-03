# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for c in range (0, 5):
    num = int(input('Digite um número: '))
    if len(lista) == 0: #se a lista estiver vazia, adc final
        lista.append(num)
    elif num < lista[0]: #se num menor que 1° item, adc num pos 0
        lista.insert(0, num)
    elif num > lista[0]: #se num maior que 1° item...
        if len(lista) == 1: #e lista tem 1 item...
            lista.append(num)# adc no final
        elif num < lista[1]:
            lista.insert(1, num)
        elif num > lista[1]:
            if len(lista) == 2:
                lista.append(num)
            elif num < lista[2]:
                lista.insert(2, num)
            elif num > lista[2]:
                if len(lista) == 3:
                    lista.append(num)
                elif num < lista[3]:
                    lista.insert(3, num)
                elif num > lista[3]:
                    lista.append(num)

print(lista)

#a solução poderia ser mais simples se a conferencia dos valores nas pos fosse feita com laço, += 1, em vez de if.