import time

valores = list()
npares = []
nimpares = []


while True:
    n = int(input('Digite um numero para sua lista: '))
    valores.append(n)



    c = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    while c not in ['S', 'N']:
        c = str(input('Quer Continuar: [S/N]')).strip().upper()[0]

    if c == 'N':
        break

for numeros in valores:
    if numeros % 2 == 0:
        npares.append(numeros)
    else:
        nimpares.append(numeros)

print(f' A lista digitada foi  {valores}')
print(f'Os valores pares dessa lista são: {npares} ')
print(f'Os valore ímpares dessa lista é: {nimpares}')
print('Finalizando aplicação ...')
time.sleep(1)
print('Aplicação Finalizada! ')

