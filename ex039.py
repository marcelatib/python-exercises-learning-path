""" Faça um programa que leia o ano de nascimento de um homem e informe, de acordo com a sua idade:
SE ele  ainda vai alistar ao serviço militar / SE É A hora de se alistar / SE JÁ PASSOU do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """
import datetime
nasc = int(input('Digite apenas o ANO do seu nascimento em quatro dígitos: '))
data_atual = datetime.date.today()
ano_atual = data_atual.year
ano_falta = data_atual.year - nasc
print('Verificando a situação de alistamento para o jovem nascido em {} ...'.format(nasc))
if nasc == ano_atual - 18:
    print('É ano de alistamento! Você tem até o dia 30/06 para se apresentar.')
elif nasc < ano_atual - 18 and ano_falta == 19:
    print('Já passou do tempo do seu alistamento!')
    print('Você está 1 ano atrasado!!')
elif nasc < ano_atual - 18:
    print('Já passou do tempo do seu alistamento!')
    print('Você está {} anos atrasado!!'.format((ano_atual - 18) - nasc))
elif nasc > ano_atual - 18 and ano_falta == 17:
    print('Não é hora do seu alistamento, mas fique atento, pois falta apenas 1 ano.')
elif nasc > ano_atual - 18:
    print('Não é hora do seu alistamento.')
    print('Ainda faltam {} anos.'.format(nasc - (ano_atual - 18)))
