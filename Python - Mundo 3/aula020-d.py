def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [4, 2, 7, 9, 6, 1]
dobra(valores)
print(valores)