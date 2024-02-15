contador = soma = 0
n = int(input(f'Digite um número (Digite 999 para encerrar): '))
while True:
    if n == 999:
        break
    contador += 1
    soma += n
    n = int(input(f'Digite um número (Digite 999 para encerrar): '))
print(f'Aplicação encerrada e foram digitados {contador} números!\n'
      f'A soma desses números é {soma}')
