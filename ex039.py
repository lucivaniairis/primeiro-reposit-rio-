from datetime import date
atual=date.today().year
nasc=int(input('Qual o ano de nascimento:'))
genero=int(input('''Digite seu gênero
[1]MASCULINO
[2]FEMININO'''))
if genero==2:
    print('Você não precisa se ALISTAR!')
if genero==1:
    idade=atual-nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade==18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade<18:
        falta=18-idade
        print('Faltam {} anos para o alistamento'.format(falta))
        ano=atual+falta
        print('seu alistamento será em {}'.format(ano))
    elif idade>18:
        saldo=idade-18
        print('Você deveria ter se alistado há {} anos'.format(saldo))
        ano=atual-saldo
        print('Seu alistamento foi em {}'.format(ano))
