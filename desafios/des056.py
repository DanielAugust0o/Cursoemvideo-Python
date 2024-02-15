soma_idades = 0
soma_mulheres = 0
idade_mais_velha = 0
nome_pessoa_mais_velha = ''

for i in range(1, 5):
    print(f'-----{i}ª PESSOA ------')
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    soma_idades += idade
    sexo = input('Digite seu sexo (m/f): ').strip()

    if sexo == 'f' and idade < 20:
        soma_mulheres += 1

    if sexo == 'm' and idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_pessoa_mais_velha = nome

media_idade = soma_idades / 4

print(f'O homem mais velho é {nome_pessoa_mais_velha} com {idade_mais_velha} anos.')
print(f'A média de idades é: {media_idade}')
int(f'O número de mulheres com menos de 20 anos é: {soma_mulheres}')