numero_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                       'Onze', 'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um numero de 0 à 20: '))

    while n < 0 or n > 20:
        n = int(input('ATENÇÃO!! Digite um numero de 0 à 20: '))

    print(f'O numero {n} por extenso é : {numero_extenso[n]}')
    break
print('Aplicação finalizada! ')
