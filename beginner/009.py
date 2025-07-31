NI = int(input('Digite um número inteiro: '))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('-' * 12)

for result in tabuada:
    print('{} x {} = {}' .format(NI, result, NI*result))
    print('-' * 12)