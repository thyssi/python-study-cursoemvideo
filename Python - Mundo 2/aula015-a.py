n = s = 0
while True: #loop infinito
    n = int(input('Um número: '))
    if n == 999:
        break
    s += n
print(s)