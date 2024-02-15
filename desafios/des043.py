
def calcular_imc(peso, altura):
    # calculando imc
    imc = peso/(altura **2)
    return imc


peso = float(input('Digite seu Peso em KG: '))
altura = float(input('Digite sua Altura em Metros: '))

imc = calcular_imc(peso, altura)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbita')