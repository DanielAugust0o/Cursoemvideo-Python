
menor_peso = float('inf')
maior_peso = float('-inf')

for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))

    # achar o menor pesso e o maior
    menor_peso = min(menor_peso, peso)
    maior_peso = max(maior_peso, peso)

#mostrar o maior peso e o menor
print(f'O pesso maior peso é {maior_peso} , \n'
      f'E o menor peso é {menor_peso}')



