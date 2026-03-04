# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite. Calcule a multa total.
velocidade = int(input('Digite a velocidade que você passou no radar com o seu carro: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Você é um motorista responsável! Mantenha-se seguro!')
else:
    print('Cuidado com a velocidade! Você passou a {} e a sua multa será de R$ {}.'.format(velocidade, multa))