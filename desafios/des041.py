from datetime import datetime

nasc = int(input('Digite o seu ano de nascimento: '))
data_atual = datetime.today().year

categoria = data_atual - nasc

if categoria <= 9:
    print('MIRIM')
elif categoria <= 14:
    print('INFANTIL')
elif categoria<= 19:
    print('JUNIOR')
elif categoria <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
