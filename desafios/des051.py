a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão de sua PA: '))

quantidade_termos = 10

for n in range(quantidade_termos):
    termo = a1 + n * r
    print(f'Termo {n+1}: {termo}')
