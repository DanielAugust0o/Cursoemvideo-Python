
print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 70)
a1 = int(input('Digite um numero para saber a Sequência Fibonacci: '))
print('-' * 70)
contador = 0
aux1 = a1
aux2 = a1 + 1

n = int(input('Quantos numeros você quer saber dessa sequência Fibonacci: '))
print('˜' * 70)
while contador < n:
    print(f'{aux1} -> ', end='')
    aux_soma = aux1 + aux2
    aux1 = aux2
    aux2 = aux_soma
    contador += 1
print('FIM')
print('-=' * 30)


