print('Gerdor de PA')
print('-=' * 20)
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = a1
contador = 1
total = 0
n = 10
while n != 0:
    total = total + n
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += r
        contador += 1
    print('PAUSA')
    n = int(input('Quantas vezes você quer executar (digite 0 para sair): '))
print('FIM')




