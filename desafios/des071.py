print('==' * 30)
print('          BANCO CEV')
print('==' * 30)

cont_cinquenta = 0
cont_vinte = 0
cont_dez = 0
cont_um = 0

while True:
    v = int(input('Que valor você quer sacar? '))

    # Verifica a quantidade de cédulas de 50
    cont_cinquenta = v // 50
    v = v % 50

    # Verifica a quantidade de cédulas de 20
    cont_vinte = v // 20
    v = v % 20

    # Verifica a quantidade de cédulas de 10
    cont_dez = v // 10
    v = v % 10

    # O restante será em cédulas de 1
    cont_um = v

    print('==' * 30)
    print(f'''  Total de {cont_cinquenta} cédulas de R$50.00
    Total de {cont_vinte} cédulas de R$20.00
    Total de {cont_dez} cédulas de R$10.00
    Total de {cont_um} cédulas de R$1.00
    ''')
    print('==' * 30)
    break

print('Volte sempre ao Banco CEV! Tenha um bom dia')
