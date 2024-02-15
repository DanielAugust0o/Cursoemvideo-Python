
#escrever o numero
n = int(input('Digite o numero que você queira converter: '))
#escolher em qual formato quer que converta
formato = str(input('Digite em qual formato você quer transfortmar(binario, octal ou hexadecimal):'))


if formato == 'binario':
    numero = bin(n)[2:]
elif formato == 'octal':
    numero = oct(n)[2:]
elif formato == 'hexadecimal':
    numero = hex(n)[2:]

print(numero)



