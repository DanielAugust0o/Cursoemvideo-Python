
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))

media =(nota1 + nota2)/2


print(f'Sua média é {media}')
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
