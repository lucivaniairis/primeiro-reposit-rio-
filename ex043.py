peso=float(input('Qual é o seu peso?(Kg)'))
alt=float(input('Qual a sua altura?(m)'))
imc=peso/(alt**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc<18.5:
    print('Você está abaixo do peso normal!')
elif 18.5<= imc<25:
    print('Você está na faixa de peso normal!')
elif 25<=imc<30:
    print('Você está em sobrepeso!')
elif 30<=imc<40:
    print('Você está em OBESIDADE!')
elif imc>=40:
    print('Você está em OBESIDADE MORBIDA!')