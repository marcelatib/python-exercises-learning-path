""" Crie um programa que leia o ano de nascimento de sete pessoas OK. No final, mostre QUANTAS PESSOAS ainda não atingiram a maior
idade e QUANTAS já são maiores. Maioridade civil e penal: 18 anos no Brasil. """
from datetime import date
ano_vigente = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = ano_vigente - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Temos \033[1;33m{}\033[m pessoas maiores de idade e \033[1;31m{}\033[m menores.'.format(maiores, menores))
