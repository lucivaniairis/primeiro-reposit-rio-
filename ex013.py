atual=float(input('Qual o salário atual do funcionário?R$'))
ajuste=atual+(atual*15/100)
print('O funcionário que recebia R${:.2f} passará a receber R${:.2f}'.format(atual, ajuste))