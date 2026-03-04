# Crie um programa que leia o nome de alguma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Marcela Ariane Tiburcio. primeiro: Marcela, último: Tiburcio.
nome = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {} e seu sobrenome é {}.'.format(nome [0], nome[-1]))