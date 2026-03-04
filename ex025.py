# Crie um programa que leia o nome de alguma pessoa a diga se ela TEM '' SILVA'' NO NOME.
nome = input('Digite um nome: ').strip()
print('SILVA' in [parte.upper() for parte in nome.split()])
