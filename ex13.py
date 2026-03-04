# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$ '))
novosalario = salario + (salario * 15 / 100)
print('O salário anterior era R$ {:.2f}. \nConsiderando o aumento de 15%, o salário passa a ser R$ {:.2f}.'.format(salario, novosalario))