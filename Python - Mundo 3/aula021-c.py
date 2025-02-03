def funcao():
    global n1 #n1 deixa de ser local e passa a ser global
    n1 = 4
    print(f'N1 local vale {n1}')

n1 = 2
funcao()
print(f'N 1 global vale {n1}')