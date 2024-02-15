import random

intervalo_inicial = 1
invervalo_final = 10
print('-=' * 20)
tamanho_tupula = 5



tupula_sorteada = tuple(random.randint(intervalo_inicial, invervalo_final) for _ in range(tamanho_tupula))

menor_valor = min(tupula_sorteada)
maior_valor = max(tupula_sorteada)



print(f'Os valore sorteados foram: {tupula_sorteada}')
print('-=' * 20)
print(f'O Menor valor sorteado foi: {menor_valor} ')
print(f'O Maior valor sorteado foi: {maior_valor} ')
