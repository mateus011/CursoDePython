#9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 

# de acordo com a tabela abaixo:

# Fórmula do IMC = peso / (altura) ²

# Tabela Condições IMC

#  Abaixo de 18,5   | Abaixo do peso          

#  Entre 18,6 e 24,9 | Peso ideal (parabéns)  

#  Entre 25,0 e 29,9 | Levemente acima do peso

#  Entre 30,0 e 34,9 | Obesidade grau I 

#  Entre 35,0 e 39,9 | Obesidade grau II (severa)

#  Maior ou igual a 40 | Obesidade grau III (mórbida)]

peso = float(input("coloque o seu peso : "))# pegando o peso atraves do input
altura = float(input("coloque a sua altura : "))  # pegando o altura atraves do input

#calcular o IMC
imc = peso / (altura * altura) 
if imc < 18.5 or imc <= 24.9:
    print("O seu imc está abaixo do peso ",imc)
elif imc == 25.0 or imc <= 29.9: 
    print("O seu imc esta levemente acima do peso",imc)
elif imc == 30.0 or imc <= 34.9:
    print("O seu imc está Obesidade grau I ",imc)
elif imc ==35.0 or imc <= 39.9:
    print("O seu  imc está Obesidade grau II (severa) " ,imc)
elif imc >= 40:
    print("O seu imc está em Obesidade grau III (mórbida)]",imc)
else:
    print("oque colocou esta fora",imc)