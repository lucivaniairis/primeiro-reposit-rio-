#opost=float(input('Digite o cateto oposto:'))
#adja=float(input('Digite o cateto adjacente:'))
#hipot=(opost**2+adja**2)**(1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hipot))
import math
co=float(input('Digite o cateto oposto:'))
ca=float(input('Digite o cateto adjacente:'))
hipot=math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipot))