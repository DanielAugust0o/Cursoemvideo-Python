def SearchingChallenge(strParam):
    palavras = strParam.split()  # irá fazer a separação das letras

    max_rep = 0

    for palavra in palavras:
        # Contar as repetições de cada letra nas palavras
        cont_letras = {}

        for letra in palavra:
            if letra.isalpha(): # ignorar caracteres não alfabéticos
                cont_letras[letra] = cont_letras.get(letra, 0) + 1

        # Verificando se a palavra tem mais repetições
        if max(cont_letras.values(), default=0) > max_rep:
            max_rep = max(cont_letras.values())
            palavra_mais_repetida = palavra

    if max_rep == 1:
        return -1
    else:
        return palavra_mais_repetida
print(SearchingChallenge(input()))
