velocidade=float(input('Qual a velocidade atual do carro:'))
if velocidade > 80:
    print('\033[32mMultado! Você excedeu o limite de volocidade que é de 80Km/h')
    multa=(velocidade-80)*7
    print('Você deverá pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')