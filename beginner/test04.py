print('oi' * 5)
print('=' * 5)


name = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!' .format(name))
print('Prazer em te conhecer {:20}!' .format(name))
print('Prazer em te conhecer {:>20}!' .format(name))
print('Prazer em te conhecer {:<20}!' .format(name))
print('Prazer em te conhecer {:^20}!' .format(name))
print('Prazer em te conhecer {:=^20}!' .format(name))



n1 = int(input('\n\nDigite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\nA soma é {}, o produto é {} e a divisão {}.' .format(s, m, d))
print('Divisão inteira {} e potência {}\n' .format(di, e))