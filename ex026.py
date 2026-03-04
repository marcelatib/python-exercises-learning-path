# Crie um programa que leia uma frase e diga quantas vezes aparece a letra A.
# em que POSIÇÃO ela aparece a primeira vez. E em que posição ela aparece a última vez.
frase = str(input('Digite a fase que você quiser: ')).strip().lower()
print('A letra A aparece {} vezes.'.format(frase.count('a')))
print('A primeira ocorrência está na posição {}'.format(frase.find('a')+1))
print('A última ocorrência está na posição {}.'.format(frase.rfind('a')+1))