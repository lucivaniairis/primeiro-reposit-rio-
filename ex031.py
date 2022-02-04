distancia=float(input('Qual é a distância da viagem:'))
print('Você está preste a iniciar uma viagem de {}Km'.format(distancia))
if distancia <= 199:
    valor=distancia*0.50
else:
    valor=distancia*0.45
print('O preço da sua passagem será de {:.2f}'.format(valor))