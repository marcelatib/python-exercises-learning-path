# Crie um programa que leia o nome de alguma cidade e diga se ela COMEÇA ou não com a palavra SANTO.
cidade = input('Digite o nome de uma cidade: ').strip().upper().split()
print(cidade[0] == 'SANTO')

