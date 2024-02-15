import datetime

nome = str(input('Digite seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))
data_atual = datetime.date.today().year

alistamento = data_atual - ano

if alistamento <= 17:
    situacao = 18 - alistamento
    print(f'{nome} Falta {situacao} anos para você se alistar! ')

elif alistamento == 18:
    print('Atenção! você terá que se alistar esse ano! Confira as datas previstas!')
else:
    situacao = alistamento - 18
    print(f'{nome} passou {situacao} anos do tempo de alistamento, se vc não se alistou procure a junta militar mais proxima')





