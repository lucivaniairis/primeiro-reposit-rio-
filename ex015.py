dias=float(input('Quantos dias o carro ficou alugado?'))
km=float(input('Quantos km foram percorridos?'))
valordia=dias*60
valorkm=km*0.15
total=valordia+valorkm
print('O valor pela quantidade de dias foi de R${:.2f}'.format(valordia))
print('O valor pela quantidade de km foi de R${:.2f}'.format(valorkm))
print('O total a pagar é de R${:.2f}'.format(total))
