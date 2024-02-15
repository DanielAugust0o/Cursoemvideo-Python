import datetime

a = int(input('Digite o Ano que você deseja saber se é bissexto (Coloque 0 para analizar o ano atual): '))
from datetime import date
if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Ano é BISSEXTO')
else:
    print('Ano não é BISSEXTO')