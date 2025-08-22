import math

num = float(input('Digite um número qualquer: '))
raiz = math.sqrt(num)

print('A raiz de {} é: {.2f}' .format(num, math.ceil(raiz))) #ceil = arredonda para cima
print('Outra representação da raiz é {}' . format(math.floor(raiz)))
