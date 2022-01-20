preco=float(input('Qual o preço do produto?$'))
desconto=preco-(preco*5/100)
print('O produto que custava R${}, na promoção com 5% de desconto vai custar R${:.2f}'.format(preco, desconto))