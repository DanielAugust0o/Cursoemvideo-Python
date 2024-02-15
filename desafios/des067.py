n = int(input('Digite o numero que gostaria de saber a tabuada: '))
s = 0

while True:
    if n < 0:
        break
    for c in range(0, 11):
        s = c * n
        print(f'{c} X {n} = {s}')
    if c == 10:
        n = int(input('Digite o numero que gostaria de saber a tabuada: [DIGITE 0 PARA SAIR] '))

print('FIM')







