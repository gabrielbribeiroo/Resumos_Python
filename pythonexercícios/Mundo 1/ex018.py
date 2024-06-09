from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('O ângulo de {:.2f} tem o seno de {}'.format(ang, sen))
print('O ângulo de {:.2f} tem o cosseno de {}'.format(ang, cos))
print('O ângulo de {:.2f} tem a tangente de {}'.format(ang, tg))
