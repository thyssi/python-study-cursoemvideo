# Faça um programa que leia uma frase pelo teclado e mostre:
#   - Quantas vezes aparece a letra "A"
#   - Em que posição ela aparece a primeira vez
#   - Em que posição ela aparece a última vez.

frase = input('Insira uma frase: ').strip()
frase_min = frase.lower()
frase_rep_til = frase_min.replace('ã','a')
frase_rep_circ = frase_rep_til.replace('â', 'a')
frase_rep_ag = frase_rep_circ.replace('á', 'a')
frase_rep_cra = frase_rep_ag.replace('à', 'a')
qntA = frase_rep_cra.count('a')
posA_first = frase_rep_cra.find('a')
posA_last = frase_rep_cra.rfind('a')

print(f'A letra "a" aparece {qntA} vezes na sua frase. A sua primeira aparição é na {posA_first+1}° ', end='')
print(f'posição e a última é na {posA_last+1}° posição.')