n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
#definindo quem é menor
menor = n1
if n1<n2 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#denindo quem é maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor numero foi {}, o maior numero foi {}'.format(menor,maior))







