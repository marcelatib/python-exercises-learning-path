"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa:
O programa deve perguntar o valor da casa, o salário do comprador e em quantos ANOS ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então, o empréstimo será negado. """
vcasa = float(input('Digite o valor da casa em R$: '))
salario = float(input('Digite o seu salário em R$: '))
anos = int(input('Digite em quantos anos irá quitar a casa em questão: '))
parcelas = anos * 12
mensal = vcasa / parcelas
if mensal <= (salario * 0.3):
    print('PARABÉNS SEU EMPRESTIMO FOI APROVADO!!')
    print('''De acordo com seu salário de R$ {:.2f}, a casa no valor de R$ {:.2f} a ser paga em {} anos, 
o valor da sua prestação será de R$ {:.2f} a ser pagos em {} parcelas.'''.format(salario, vcasa, anos, mensal, parcelas))
else:
    print('Sinto informar, mas o seu empréstimo foi negado.')
    print('''O valor da casa em R$ {:.2f} a ser pago em {} anos, tendo em vista o seu salário de R$ {:.2f} excede em 30% do valor da parcela.'''.format(vcasa, anos, salario))
