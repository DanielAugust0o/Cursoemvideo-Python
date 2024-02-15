valores = list()
cont = 0
cont_cinco = 0
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    cont += 1

    if v == 5:
        cont_cinco += 1

    c = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]

    while c not in ['S', 'N']:
        c = str(input('ATENÇÃO DIGITE UM VALOR VÁLIDO! Quer Continuar: [S/N]')).strip().upper()[0]
    if c == 'N':
        break

print(f'Você digitou {cont} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if cont_cinco > 0:
    print(f'O valor 5 faz parte da lista e apareceu {cont_cinco} vezes')
else:
    print('O valor cinco não faz parte da lista')