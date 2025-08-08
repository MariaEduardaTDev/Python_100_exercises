import math

print('Esse programa irá calcular e exibir o comprimento da hipotenusa de um triângulo retângulo!\n')
unM = input('Digite a sua unidade de medida utilizada (ex: cm, m, mm): ')
catA = int(input('Digite o comprimento do cateto adjacente de um dos ângulos agudos: '))
catO = int(input('Digite o comprimento do cateto oposto à esse ângulo: '))

catA2 = math.pow(catA, 2)
catO2 = math.pow(catO, 2)

hip = math.sqrt(catA2 + catO2)

print('\nO comprimento da hipotenusa do seu triângulo retângulo é de {:.2f}{}.' .format(hip, unM))