nota1=float(input('Primeira nota:'))
nota2=float(input('Segunda nota:'))
media=(nota1+nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2, media))
if media>=7:
    print('O aluno está aprovado!')
elif media>=5 and media<7:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')


