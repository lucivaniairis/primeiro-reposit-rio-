linguas={'br':'portugues', 'eua':'ingles'}
print(type(linguas))
print(linguas)
print(linguas['br'])
print('br'in linguas)
linguas['es']="espanhol"
print(linguas['es'])
for chave in linguas:
    print(chave)
for valor in linguas.values():
    print(valor)
for chave, valor in linguas.items():
    print(chave, valor)
linguas.pop('br')
print(linguas)
del linguas['eua']
print(linguas)