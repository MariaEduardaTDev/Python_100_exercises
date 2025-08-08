days = int(input('Digite a quantidade de dias que o carro foi alugado: '))
vDays = days * 60
km = float(input('Digite a qauntidade de km rodados: '))
vKm = km * 0.15

vTotal = vDays + vKm
print('O valor a ser pago é: R${:.2f}' .format(vTotal))