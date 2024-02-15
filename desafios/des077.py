palavras = ('aprender', 'programar', 'linguagem','python', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for pos in range(len(palavras)):
    palavra = palavras[pos]
    vogais = [v for v in palavra if v.lower() in 'aeiou']
    print(f'Na palavra {palavra.upper()} temos {" ".join(vogais)}')
