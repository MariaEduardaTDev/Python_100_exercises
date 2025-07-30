alt = float(input('Digite a altura da sua parede (em metros): '))
larg = float(input('Digite a largura da sua parede (em metros): '))
area = alt*larg
tinta = area/2

print('A Área total da parece é de {:.2f} m² e será necessário {:.2f} litros de tinta.' . format(area, tinta))