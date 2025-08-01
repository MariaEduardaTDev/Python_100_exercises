grausC = int(input('Digite uma temperatura em graus Celsius (ºC): '))
grausF = (grausC * (9/5)) + 32
grausF2 = int(input('Digite uma temperatura em Fahrenheit (ºF): '))
grausC2 = (grausF2 - 32) * (5/9)
print('A sua temperatura de {}ºC equivale {} Fahrenheit (ºF)' .format(grausC, grausF))
print('A sua temperatura de {}ºF equivale {} Celsius (ºC)' .format(grausF2, grausC2))