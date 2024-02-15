cont = 0
numeros = []
nove = '9'
cont_nove = 0
n = 0

while cont < 4:
    cont += 1
    numero = int(input(f'Digite o {cont}º numero: '))
    numeros.append(numero)

tupula_numeros = tuple(numeros)
print('-=' * 20)
print(f'Você digitou os valores {tupula_numeros}')
print('-=' * 20)
for numero in tupula_numeros:
    if numero == 9:
        cont_nove += 1
    if 3 in tupula_numeros:
        n = tupula_numeros.index(3)
        p = n + 1
        n = (f'se encontra na {p}ª posição ')
    else:
        n = 'não foi digitado em nenhuma posição'

    par = tuple(numero for numero in tupula_numeros if numero % 2 == 0)

print(f'O valor 9 apareceu {cont_nove} vezes')
print('-=' * 20)
print(f'O valor 3 {n}')
print('-=' * 20)
print(f'Os valores pares digitados foram: {par}')
print('-=' * 20)




