from datetime import date
contmaior = 0
contmenor = 0
atual = date.today().year
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade = atual - nasc
    if idade < 18:
        contmenor += 1
    else:
        contmaior += 1

print(f'Nessa lista possui {contmenor} menor de idade\n'
      f'E também  possui {contmaior} pessoas maiores de idade')







