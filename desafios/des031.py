d = float(input('Digite a distância de sua viagem? '))
print('Voce irar começar uma viagem de {}KM '.format(d))
print('-=-' * 20)
dt = 0
if d <= 200:
    dt = 0.5 * d
if d > 200:
    dt = 0.45 * d
print('Será cobrado R${:.2f} a viagem '.format(dt))
print('-=-' * 20)
