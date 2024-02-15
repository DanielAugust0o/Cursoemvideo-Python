nomes_times = (
    'Palmeiras',
    'Grêmio',
    'Atlético-MG',
    'Flamengo',
    'Botafogo',
    'Bragantino',
    'Fluminense',
    'Athletico-PR',
    'Internacional',
    'Fortaleza',
    'São Paulo',
    'Cuiabá',
    'Corinthians',
    'Cruzeiro',
    'Vasco',
    'Bahia',
    'Santos',
    'Goiás',
    'Coritiba',
    'América-MG',
)
time_procurado = 'São Paulo'

print(f'Os 5 primeiros colocados são: {nomes_times[0:5]}')
print('-=' * 20)
print(f'Os ultimos 4 colocados é: {nomes_times[-4:]}')
print('-=' * 20)
print(f'A lista com nomes dos times em ordem alfabética é : {sorted(nomes_times)}')
print('-=' * 20)
if time_procurado in nomes_times:
    posicao = nomes_times.index(time_procurado)
    posicao += 1

print(f'O São Paulo se encontra na {posicao}º do Campeonato Brasileiro')
print('-=' * 20)