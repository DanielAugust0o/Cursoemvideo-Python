from random import choice
alunoum = str(input("Digite o nome do aluno um: "))
alunodois = str(input("Digite o nome do aluno dois: "))
alunotres = str(input("Digite o nome do aluno tres: "))
alunoquatro = str(input("Digite o nome do aluno quatro: "))
lista = [alunoum, alunodois, alunotres, alunoquatro]
escolhido = choice(lista)
print("O Aluno escolhido foi {}:".format(escolhido))

