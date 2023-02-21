#co = float(input('Cumprimento do cateto oposto: '))
#ca = float(input('Cumpimento do cateto adjacente: '))
#hi = ( co ** 2 + ca ** 2 ) ** (1/2)
#print('A hipotenusa vai medir {:.2f}. '.format(hi))

from math import hypot
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumpimento do cateto adjacente: '))
hi = hypot (ca, co)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

