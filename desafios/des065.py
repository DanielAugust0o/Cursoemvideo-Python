contador = 0
soma =0
maior = float('-inf')
menor = float('inf')
igual = 'Igual'

while True:
    n = int(input(f'Digite o {contador + 1}º numero: '))
    soma +=n

    if n > maior:
        maior = n
    if n < menor:
        menor = n


    continuar = str(input('Deseja continuar digitando: [S/N] ')).strip().upper()[0]
    contador += 1

    if continuar != 'S':
        media = soma / contador
        print(f'Você digitou {contador} numeros e a media foi {media}')
        if maior == menor:
            print('Não tem maior nem menor os numeros são iguais!')
        else:
            print(f'O maior valor foi {maior} e o menor valor foi {menor}')
            break



