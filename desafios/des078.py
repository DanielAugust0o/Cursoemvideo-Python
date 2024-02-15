valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para Posição {cont}: ')))
    cont += 1

print('=-'*30)
print(f'Os Valores digitados foram: {valores}')
print('=-'*30)

min_valor = min(valores)
index_min_valor = valores.index(min_valor)
print(f'O menor valor é {min_valor} e se encontra na {index_min_valor + 1}ª Posição')

max_valor = max(valores)
index_max_valor = valores.index(max_valor)
print(f'O maior valor é {max_valor} e se encontra na {index_max_valor + 1}ª Posição')





# valores.sort()
# print(f'O menor valor digitado foi: {valores[0]}')
# valores.sort(reverse=True)
#