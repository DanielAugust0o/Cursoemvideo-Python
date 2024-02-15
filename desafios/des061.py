print('Gerdor de PA')
print('-=' * 10)
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = a1
contador = 1
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    contador += 1
print('FIM')