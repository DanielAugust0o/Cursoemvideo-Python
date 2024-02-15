v = float(input('Digite a velocidade do carro:'))

if v > 80:
    m = (v - 80) * 7
    print('Você foi multado! e pagará R${:.2f} de multa'.format(m))
else:
    print('Pode ficar tranquil120o você não foi multado')