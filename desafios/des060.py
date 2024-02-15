n = int(input('Entre com um numero que você queira saber o fatorial :'))
resultado = 1
print(f'{n}! = ', end='')

while n > 0:
    resultado *= n
    print(f'{n}', end='')
    if n > 1:
        print(' x ', end='')
    n -= 1
print(f' = {resultado}')