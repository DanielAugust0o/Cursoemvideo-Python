import time
from time import sleep
n1 = int(input('Digite o Primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
o = 0
print('-=-' * 20)

while o != 5:
    print('''
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NUMEROS
        [ 5 ] EXIT ''')
    o = int(input('>>>>>>> Qual é a sua Opção? '))
    if o == 1:
        r = n1 +n2
        print(f'A soma entre {n1} + {n2} = {r}')
        print('-=-' * 20)
    elif o == 2:
        r = n1 * n2
        print(f'A Multiplicação de {n1} X {n2} = {r}')
        print('-=-' * 20)
    elif o == 3:
        if n1 == n2:
            print('Os numeros são iguais!!')
        elif n1 > n2:
            print(f'O maior numero é {n1} e o menor é {n2}')
        else:
            print(f'O maior numero é {n2} e o menor é {n1}')
        print('-=-' * 20)
    elif o == 4:
        print('-=-' * 20)
        n1 = int(input('Digite o Primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif o == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('-=-' * 20)
    sleep(2)
print('Aplicação finalizada! Volte Sempre')








