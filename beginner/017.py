import math
print('\nEsse programa calculará e exibirá os valores do Seno, Cosseno e Tangente de um ângulo qualquer!\n')

graus = int(input('Digite o valor do ângulo em graus: '))
grausRadian = math.radians(graus)
seno = math.sin(grausRadian)
cosseno = math.cos(grausRadian)



if abs(cosseno) < 1e-10: 
    tangente = math.tan(grausRadian)
else:
    tangente = 'indefinida'


print('O seno de {}° é: {:.2f}' .format(graus, seno))
print('O cosseno de {}° é: {:.2f}' .format(graus, cosseno))
print('A tangente de {}° é: {}' .format(graus, tangente))
