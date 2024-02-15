import random


print('-=-' * 20)
print('JO\nKEN\nPÔ')
print('-=-' * 20)
jogada = str(input('Escolha entre pedra, papel ou tesoura: '))
print('JO\nKEN\nPÔ')

print('-=-' * 20)
minha_lista = ['pedra', 'papel', 'tesoura']
sorteado = random.choice(minha_lista)
print('-=-' * 20)
print(f'O computador escolheu {sorteado}')

print('-=-' * 20)
#possibilidades de ganhar
if jogada == 'pedra' and sorteado == 'tesoura':
    print('Parabéns você ganhou, pedra quebra tesoura')
elif jogada == 'tesoura' and sorteado == 'papel':
    print('Parabéns você ganhou, tesoura corta papel')
elif jogada == 'papel' and sorteado == 'pedra':
    print('Parabens você ganhou, papel embrulha pedra')
#possibilidades de perder
elif sorteado == 'pedra' and jogada == 'tesoura':
    print('Infelizmente você perdeu, pedra quebra tesoura')
elif sorteado == 'tesoura' and jogada == 'papel':
    print('Infelizmente você perdeu, tesoura corta papel')
elif sorteado == 'papel' and jogada == 'pedra':
    print('Infelizmente você perdeu, papel embrulha pedra')
else:
    print('Vocês Empataram')
print('-=-' * 20)


