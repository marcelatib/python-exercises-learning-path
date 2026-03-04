# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
# 1 - PERGUNTAR ao usuário a quantidade de KM percorridos.
# 2 - PERGUNTAR ao usuário quantos dias o carro foi alugado.
# 3 - CALCULAR e dizer o preço a pagar pelo aluguel do carro com base nas informações acima dadas pelo usuário.
km = float(input('Informe os KM percorridos com o carro: '))
dias = int(input('Informe a quantidade de dias que alugou o carro: '))
total = (dias * 60) + (km * 0.15)
print('Você ficou {} dias com o carro e percorreu {} KM. \nValor a pagar R$ {:.2f}.'.format(dias, km, total))
