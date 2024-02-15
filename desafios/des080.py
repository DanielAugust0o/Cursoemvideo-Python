valores = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))

    if cont == 0 or n > valores[-1]:
        print('Adicionado ao final da lista...')
        valores.append(n)
    else:
        for i, valor in enumerate(valores):
            if n <= valor:
                print(f'Adicionado na posição {i} da lista...')
                valores.insert(i, n)
                break

print(f'Os valores digitados em ordem: {valores}')
