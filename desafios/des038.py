n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O {n1} é maior que o numero {n2} ')
elif n2 > n1:
    print(f'O {n2} é maior que o numero {n1}')
else:
    print('Não existe valor maior , os dois são iguais')
