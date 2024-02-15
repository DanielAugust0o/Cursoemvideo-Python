nome = str(input('Qual é seu nome: '))
if nome == 'Daniel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')

else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia \033[2;35;41m{}\033[m!'.format(nome))
