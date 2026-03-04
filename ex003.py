#Fazer o sistema pedir ao usuário para digitar dois numeros e fazer a soma deles printando o resultado.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1 + n2
print('A soma de {:.0f} e {:.0f} é {:.0f}.'.format(n1, n2, soma))
