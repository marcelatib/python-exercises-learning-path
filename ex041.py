""" A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
de acordo com a sua idade: ATÉ 9 anos: Mirim / ATÉ 14 anos: Infantil / ATÉ 19 anos: Junior / ATÉ 20 anos: Sênior / Acima: Master. """
import datetime
nasc = int(input('Digite o ANO do seu nascimento no formato de quatro dígitos: '))
data_a = datetime.date.today()
ano_a = data_a.year
idade = ano_a - nasc
if idade >= 0 and idade <= 9:
    print('Sua idade é {} anos. Categoria: MIRIM.'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Sua idade é {} anos. Categoria: INFANTIL.'.format(idade))
elif idade >= 15 and idade <= 19:
    print('Sua idade é {} anos. Categoria: JÚNIOR.'.format(idade))
elif idade == 20:
    print('Sua idade é {} anos. Categoria: SÊNIOR.'.format(idade))
elif idade > 20 and idade < 120:
    print('Sua idade é {} anos. Categoria: MASTER.'.format(idade))
else:
    print('Inválido.')