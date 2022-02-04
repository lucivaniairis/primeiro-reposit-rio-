casa=float(input('Valor da casa:R$'))
comprador=float(input('Qual o salário do comprador:R$'))
anos=int(input('Quantos anos de financiamento?'))
prestacao=casa/(anos*12)
minimo=comprador*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao<=minimo:
    print('Empréstimo pode ser Concedido!')
else:
    print('EMPRÉSTIMO NEGADO!')