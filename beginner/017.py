import math

print('\nEsse programa irá calcular o Seno, Cosseno e Tangente de um ângulo qualquer.\n')

ang = int(input('Digite o valor do ângulo em graus: '))
angR = math.radians(ang)

seno = math.sin(angR)
cosseno = math.cos(angR)
tangente = math.tan(angR)


print('seno = {:.2f}' .format(seno))
print('cosseno = {:.2f}' .format(cosseno))

if cosseno < 1e-10:
    print('\ntangente = indefinida.')

else:
    print('tangente = {:.2f}' .format(tangente))

