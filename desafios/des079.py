import time
valores = []

while True:
    novo_valor = int(input('Digite um valor: '))

    if novo_valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(novo_valor)
        print("Valor adicionado com sucesso...")

    c = str(input('Quer Continuar: [S/N]')).strip().upper()[0]

    while c not in ['S', 'N']:
        c = str(input('Quer Continuar: [S/N]')).strip().upper()[0]

    if c == 'N':
        break


print('=-' * 30)
print(f'Você digitou os valores {valores}')
time.sleep(1)
print('Finalizando Aplicação...')
time.sleep(1.5)
print('Aplicação Finalizada!')
