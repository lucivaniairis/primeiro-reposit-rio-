dist=int(input('Digite uma distância em Metros:'))
km=dist/1000
hm=dist/100
dam=dist/10
dm=dist*10
cm=dist*100
mm=dist*1000
print('A medida de {} corresponde a: \n{}KM (Quilômetros)\n{}hm (Hectômetros)\n{}dam (Decametro)\n{}dm (Decimetro)\n{}cm (Centímetros)\n{}mm (Milímetros)'.format(dist, km, hm, dam, dm, cm, mm))