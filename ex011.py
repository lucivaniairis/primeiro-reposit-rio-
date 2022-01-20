larg=float(input('Digite a Largura da parede:'))
alt=float(input('Digite a Altura da parede:'))
metros=larg*alt
tinta=metros/2
print('Sua parede tem a Dimensão de {:.1f}x{:.1f} e sua área é de {:.3f}m²'.format(larg, alt, metros))
print('Você irá precisar de {:.1f}L para pintar essa parede'.format(tinta))