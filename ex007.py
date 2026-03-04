#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# Tomar cuidado com o resultado e lembrar da ordem de precedência.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('As notas digitadas foram {} e {}.\nSua média é {}.'.format(n1, n2, m))
