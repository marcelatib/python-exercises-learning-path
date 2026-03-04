"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média
atingida: Média abaixo de 5: REPROVADO / entre 5 e 6,9: RECUPERAÇÃO / Média igual ou superior a 7: APROVADO """
n1 = float(input('Digite a primeira nota de 0 a 10: '))
n2 = float(input('Digite a segunda nota de 0 a 10: '))
m = (n1 + n2) / 2
print('Avaliando a situação das notas {} e {}.'.format(n1, n2))
print('Sua média é {}.'.format(m))
if m < 5:
    print('REPROVADO!')
elif m >= 5 and m <= 6.9:
        print('RECUPERAÇÃO!')
else:
    print('APROVADO!')