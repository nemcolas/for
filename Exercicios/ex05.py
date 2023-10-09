"""Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as
suas notas e exiba a sua respectiva média (a média deve ser arredondada para duas casas decimais)."""

quantidade_alunos = int(input("Informe a quantidade de alunos: ")) #Pede a quantidade de aluno


for quantidade_alunos in range(quantidade_alunos): # looping da quantidade de aluno
    quantidade_notas = int(input("Informe a quantidade de notas :")) #Pede a quantidade de notas
    for quantidade_notas in range(quantidade_notas): # Outro looping, dessa vez vai pedir as notas do aluno pelo input q ele deu anteriormente
        notas = float(input("Informe sua nota: ")) #Aluno botando a nota
        notas += notas #Notas sendo somadas
    media = notas / quantidade_notas #notas somadas dividido pela quantidade de notas informadas
    print(f"Sua média é de: {media :.2f}") #FINALMENTE A MEDIA

