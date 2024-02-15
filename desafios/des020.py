from random import shuffle
alunoum = str(input("Digite o nome do aluno um: "))
alunodois = str(input("Digite o nome do aluno dois: "))
alunotres = str(input("Digite o nome do aluno tres: "))
alunoquatro = str(input("Digite o nome do aluno quatro: "))
lista = [alunoum, alunodois, alunotres, alunoquatro]
shuffle(lista)
print("A ordem de apresentação é: ")
print(lista)

