""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
à vista dinheiro/pix: 10% de desconto/ à vista crédito ou débito: 5% desconto / até 2x crédito: preço normal/ 3x ou mais crédito: 20% de juros. """
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção desejada? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20  / 100)
    totparcela = int(input('Quantas parcelas deseja? '))
    parcela = total / totparcela
    print ('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparcela, parcela))
else:
    total = preco
    print('\033[1;31mOPÇÃO INVÁLIDA.\033[m Tente novamente.')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))