from random import shuffle
# um professor quer sortear a ordem de apresentação de 4 alunos, apresente um programa que o faça, mostrando o aluno
# e a ordem sorteada
aluno1 = input('Digite o nome de um aluno: ')
aluno2 = input('Digite o nome do outro aluno: ')
aluno3 = input('Novamente: ')
aluno4 = input('mais uma vez: ')
a = [aluno1, aluno2, aluno3, aluno4]
shuffle(a)
print(a)
