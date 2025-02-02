# Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente. 

valor1 = 0 # três valores inteiros
valor2 = 0
valor3 = 0
valores = []
#receber os valores 
print("coloque tres valores , para visualizar na seguencia  descrecente")
valor1 = int(input("coloque o  primeiro valor : "))
valor2 = int(input("coloque o segundo valor : "))

#verificar se são diferentes
if valor1 != valor2 :
    valor3 = int(input("coloque o terceiro  valor : "))
    if valor3 != valor1 and valor3 != valor2:
        valores = valor1,valor2,valor3
        print("os valores em ordem crescente",valores)
        print("os valores em ordem decrecente",list(reversed(valores)))
 #revertendo valores list converte os valores para lista, e reversed inverte para decrescente
    else:
        print("O terceiro numero deve ser diferente dos primeiros numeros ")
  
else:

        print("os valores sao  iguais :", valor1 ,valor2)








    




  












       




 

    
        





        

         
        

    
