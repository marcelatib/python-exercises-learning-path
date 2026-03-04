""" Desenvolva uma lógica que leia o peso e altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
menor 18,5: Abaixo do peso /De 18,5 a 25: Peso ideal /De 25 a 30: Sobrepeso / Entre 30 e 40: Obesidade / Acima de 40: Obesidade Mórbida. """
peso = float(input('Qual é o seu peso em KG? '))
altura = float(input('Qual a sua altura (em metros)? '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5 :
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('CUIDADO! Você está em obesidade.')
else:
    print('ATENÇÃO! Você está em obesidade mórbida.\nProcure um médico.')