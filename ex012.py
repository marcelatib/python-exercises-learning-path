# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
antigo = float(input('Preço anterior do produto: R$ '))
atual = antigo - (antigo * 5 / 100)
print('O preço antigo do produto era R$ {:.2f}.\nConsiderando o desconto de 5%, o preço atualizado do produto é R$ {:.2f}.'.format(antigo, atual))
