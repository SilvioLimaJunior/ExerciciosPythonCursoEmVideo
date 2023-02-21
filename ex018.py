#import math
#an = float(input('Qual é o angulo?  '))
#seno = math.sin(math.radians(an))
#print('O angulo de {} tem o SENO de {:.2f} '.format(an, seno))
#cos = math.cos(math.radians(an))
#print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
#tan = math.tan(math.radians(an))
#print('O angulo de {} tem o TANGENTE de {:.2f}'.format(an, tan))

from math import sin, radians, cos, tan
an = float(input('Qual é o angulo?  '))
seno = sin(radians(an))
print('O angulo de {} tem o SENO de {:.2f} '.format(an, seno))
cos = cos(radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(an, tan))

