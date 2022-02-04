atual=float(input('Qual o salário do funcionário?'))
if  atual <= 1250:
    novo= atual+(atual*15/100)
else:
    novo=atual+(atual*10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(atual,novo))
