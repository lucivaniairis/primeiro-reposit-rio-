from random import randint
from time import sleep
print('=-'*20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('=-'*20)
jogador=int(input('Em que número que pensei:'))
print('Processando...')
sleep(1)
computador=randint(0, 5)
if jogador == computador:
    print('Parabéns você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}.'.format(computador, jogador))





