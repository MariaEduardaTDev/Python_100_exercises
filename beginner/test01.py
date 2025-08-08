import math

num = float(input('Digite um número qualquer: '))
root = math.sqrt(num)
roundUp = math.ceil(root)
roundDown = math.floor(root)
integer = math.trunc(root)
exponentiation = math.pow(root, 2)
print('A raíz quadradra de {} é: {:.1f}.' .format(num, root))
print('O arredondamento para cima da raiz de {} é: {}. \n E para baixo: {}.' .format(num, roundUp, roundDown))
print('Valor vírgula a diante: {}.' .format(integer))
print('Resultado de {:.1f} em potência quadrada: {:.1f}.' .format(root, exponentiation))
