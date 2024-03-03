def StringChallenge(num):
    horas = num // 60  # Achando quantas horas possui na entrada
    minutos = num % 60  # Achando quantos minutos possuí na entrada

    # Retornando a informação já formatada
    return f"{horas}:{minutos}"

# keep this function call here
print(StringChallenge(int(input())))
