# ler idade e sexo
# perguntar se deseja ou nao continuar para cada pessoa
# mostrar  quantas pessoas tem mais de 18 anos, quantos homens, quantas mulheres tem menos de 20 anos

cont = 0
contp = 0
conts = 0
contm = 0
while True:
    print('_' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)

    i = int(input('Idade: '))
    if i > 18:
        contp += 1

    s = str(input('Sexo: [M/F] ')).strip().upper()
    if s == 'M':
        conts += 1

    while s != 'M' and s != 'F':
        s = str(input('Sexo: [M/F] ')).strip().upper()
    print('-' * 30)

    if s == 'F' and i < 20:
        contm += 1

    c = (str(input('Quer continuar? [S/N] '))).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = (str(input('Quer continuar? [S/N] '))).strip().upper()[0]

    if c == 'S':
        cont += 1
    else:
        break

print('======= FIM DO PROGRAMA =======')
print(f'Total de Pessoa com mais de 18 anos: {contp}')
print(f'Ao todo temos {conts} homens cadastrados')
print(f'E temos {contm} mulheres com menos de 20 anos')

