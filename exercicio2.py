# 15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em 

# consideração o ano com 365 dias e o mês com 30 dias.

# (Ex: 5 anos, 2 meses e 15 dias de vida)

dia = int(input("coloque o dia que você nasceu: "))
mes = int (input("Coloque o mês que você nasceu: "))
ano = int(input("Coloque o ano que vc nasceu: " ))

#processamento 
totalAnos = 2025 - ano 
TotalDias = totalAnos * 365 
TotalMeses = totalAnos *12


print(totalAnos,"anos: ", TotalMeses, " meses: ",TotalDias, " dias: ")
