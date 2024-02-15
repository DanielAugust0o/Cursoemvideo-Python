print('-=-' * 20)
vp = float(input('Digite o valor do produto R$:'))
print('-=-' * 20)

print('-=-' * 20)
pg = int(input('\n||Digite 1 para pagamento à vista/cheque ||\n'
               '||2 para pagamento à vista no cartão     ||\n'
               '||3 para pagamento parcelado 2x no cartão||\n'
               '||4 para pagamento parcelado 3x no cartão: '))
print('-=-' * 20)
print('-=-' * 20)
if pg == 1:
    vt = vp * 0.9
    print('O valor do produto é R${:.2f}'.format(vt))
elif pg == 2:
    vt = vp * 0.95
    print('O valor do produto é R${:.2f}'.format(vt))
elif pg == 3:
    vt = vp
    print('O valor do produto é R${:.2f}'.format(vt))
elif pg == 4:
    vt = vp * 1.2
    print('O valor do produto é R${:.2f}'.format(vt))
else:
    print('Insira uma forma de pagamento valida!')



