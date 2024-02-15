import random

print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)

cont = 0

while True:
    n = int(input('Digite um Valor de 0 à 10: '))
    print('=-' * 20)
    pi = str(input('Par ou Ímpar: ')).strip().upper()[0]
    print('=-' * 20)
    jc = random.randint(0, 10)
    s = n + jc

    print(f'Você jogou {n} e o computador {jc}. Total de {s}', end=' ')

    # Verifica se o resultado é par ou ímpar
    resultado = 'P' if s % 2 == 0 else 'I'

    # Verifica se o usuário venceu ou perdeu
    if pi == resultado:
        print(f'DEU {resultado.upper()}')
        print('Você VENCEU!\nVamos jogar novamente...')
        cont += 1
    else:
        print(f'DEU {("PAR" if resultado == "I" else "IMPAR").upper()}')
        print('Você PERDEU!')
        break

    print('=-' * 20)

print(f'GAME OVER! Você venceu {cont} vezes')
