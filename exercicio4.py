# 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
num1 = 0
num2 = 1
n = int(input("coloque a quantidade de numeros que deseja : "))
for i in range(n):  # laço for para gerar sequencia de fibonacci
 print(num1, end=", ") #imprime na tela  o num1 , na mesma linha 
 num3 = num1 + num2  #  num 3=1 ,num1= 0 ,num 2 = 1     
 num1 = num2        # num1 = 1 , num2 = 1
 num2 = num3       # num2 =1 , num3 = 1

 