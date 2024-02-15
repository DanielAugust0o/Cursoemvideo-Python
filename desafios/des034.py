s = float(input('Digite o seu salário: '))

if s > 1250:
    ns = s + (s * 0.10)
else:
    ns = s + (s * 0.15)

print('O Seu salario será: R${:.2f}'.format(ns))
