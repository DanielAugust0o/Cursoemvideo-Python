import random
n = float(input('Pense em um numero de 0 à 5: '))
x = random.randint(0,5) # faz o computador sortear um numero nesse intervalo
print('-=-' * 20)
if n > 5:
    print('Digite um numero válido!')
    exit()
if n == x:
    print('Você acertou o numero!!')
else:
    print('Você errou o numero! QUE PENA! O numero sorteado foi {}!'.format(x))
print('-=-' * 20)
print('---FIM---')
