sp = 0
for c in range(1,7):
    v = float(input('Digite um valor: '))
    if v % 2 == 0:
        sp += v
print(f'A soma de todos os numeros pares é {sp}')
