# Escreva um programa que pergunte o salário de um funcuionário e calcule o valor do seu aumento.
# Para salários acima de R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do seu salário em R$: '))
if salario > 1250:
    aumento = (((salario * 0.1) / 1) + salario)
else:
    aumento = (((salario * 0.15) / 1) + salario)
print('O valor do seu salário que era de R$ {:.2f} aumentou para R$ {:.2f}.'.format(salario, aumento))