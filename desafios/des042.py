
print('-=-' * 20)
print('ANALIZADOR DE TRIANGULOS')
print('-=-' * 20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
print('-=-' * 20)
t1 = (r2 + r3) - r1
t2 = (r3 + r1) - r2
t3 = (r2 + r1) - r3


if t1 > 0 and t2 > 0 and t3 > 0:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('Esse triangulo é Equilatero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Esse triangulo é Isosceles')
    elif r1 != r2 != r3:
        print('Esse triangulo é Escaleno')
    print('-=-' * 20)

else:
    print('-=-' * 20)
    print('Infelizmente não é possivel de formar um triangulo')
    print('-=-' * 20)




