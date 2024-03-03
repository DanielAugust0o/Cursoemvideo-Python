def FirstFactorial(num):
    resultado = 1
    # Multiplica números de 1 a num
    for i in range(1, num + 1):
        resultado *= i

    return resultado

# mantendo a funcao da chamada
print(FirstFactorial(input(4)))
