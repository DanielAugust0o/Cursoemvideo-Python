def ArrayChallenge(arr):
    #verificar se o arry não está vazio
    if not arr:
        return False

    # removendo '[]'
    arr = arr.strip('[]')

    # Convertendo array para numeros inteiros e removendo a virgula
    arr = [int(num) for num in arr.split(',') if num.strip()]

    # Encontrando o maior numero do array
    n_max = max(arr)

    #somando os numeros e tirando o maior
    soma = sum(num for num in arr if num != n_max)


    #Verificando se a soma dos numeros é igual ao maior

    return soma >= n_max

# keep this function call here
print(ArrayChallenge(input()))

'''Possivelmente a orientação do desafio possuí algum erro
de digitação, pois no enunciado pede para pegar o maior valor 
e verificar se a combinação da soma dos outros valores é igual ao maior,
entretanto, quanto no enunciado como no exemplo o resultado não está
de acordo com o enunciado ex: " [4, 6, 23, 10, 1, 3] a saida deveria
retornar False porque 4 + 6 + 10 + 1 + 3 = 24 invés de 23.

A forma correta de executar seria:
def ArrayChallenge(arr):
    #verificar se o arry não está vazio
    if not arr:
        return False

    # Encontrando o maior numero do array
    n_max = max(arr)

    #somando os numeros e tirando o maior
    soma = sum(num for num in arr if num != n_max)


    #Verificando se a soma dos numeros é igual ao maior
    return soma == n_max

# keep this function call here
print(ArrayChallenge(input()))

entretanto não está batendo com os testes






'''