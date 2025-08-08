grausC = float(input('Digite uma temperatura em graus Celsius (°C): '))
grausF = (grausC * (9/5)) + 32
grausF2 = float(input('Digite uma temperatura em Fahrenheit (°F): '))
grausC2 = (grausF2 - 32) * (5/9)
print('A sua temperatura de {}ºC equivale {:.1f} Fahrenheit (°F)' .format(grausC, grausF))
print('A sua temperatura de {}ºF equivale {:.1f} Celsius (°C)' .format(grausF2, grausC2))