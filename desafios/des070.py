# ler o nome e preço de varios produtos
# perguntar se vai continuar
# motstrar o tempo gasto na compra, quantos produtos custam mais de 1000, qual o nume do produto mais barato
print('__' * 20)
print('          LOJA SUPER BARATÃO')
print('--' * 20)

cont = 0
contp = 0

menor_preco = float('inf')
nome_menor_preco = ''
sc = 0
while True:

    n = str(input('Nome do Produto: '))

    p = float(input('Preço: R$'))
    sc += p
    if p > 1000:
        contp +=1

    if p < menor_preco:
        menor_preco = p
        nome_menor_preco = n

    c = str(input('Quer Continuar: [S/N]')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('Quer Continuar: [S/N]')).strip().upper()[0]
    if c == 'S':
        cont +=1
        print('--' * 20)
    else:
        break

print('----------- FIM DO PROGRAMA -------------')
print('O total da compra foi R${:.2f}'.format(sc))
print(f'Temos {contp} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_menor_preco.capitalize()} que custa R${menor_preco:.2f}')

