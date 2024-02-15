contador = soma = 0
n = int(input(f'Digite um número (Digite 999 para encerrar): '))
while n != 999:
    contador += 1
    soma += n
    n = int(input(f'Digite um número (Digite 999 para encerrar): '))
print(f'Aplicação encerrada e foram digitados {contador} números!\n'
      f'A soma desses números é {soma}')
