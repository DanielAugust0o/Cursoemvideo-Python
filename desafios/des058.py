import random

n = float(input('Pense em um número de 0 a 10: '))
x = random.randint(0, 10)  # faz o computador sortear um número nesse intervalo
tentativas = 0
print('-=-' * 20)

if n > 10 or n < 0:
    print('Digite um número válido entre 0 e 10!')
else:
    while n != x:
        print('Você errou o número! QUE PENA! O número sorteado foi {}!'.format(x))
        x = random.randint(0, 10)  # faz o computador sortear um número nesse intervalo
        n = float(input('Pense em um número de 0 a 10: '))
        tentativas += 1
    print('-=-' * 20)
    print(f'Você acertou o número, e precisou de {tentativas} tentativas para isso!!')
