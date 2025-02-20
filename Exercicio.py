#  Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 

#  se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.
NomeAluno = "mateus"
nota1 = 6
nota2 = 7
nota3 = 6
nota4 = 7

#calculando a medias das notas
media = (nota1 + nota2+ nota3+ nota4)/4
# verificando se foi ou nao aprovado 
if media >= 7:
    aprovado = "aprovado"
    print(" O Aluno ",NomeAluno ,", sua média e ", media,"e foi ",aprovado )
else:
    reprovado = "Reprovado" 
    print("O Aluno ",NomeAluno ,", sua média e ", media,"e foi ", reprovado)
    
