# Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente. 

valor1 = 0 # três valores inteiros
valor2 = 0
valor3 = 0
#receber os valores 
print("coloque tres valores , para visualizar na seguencia  descrecente")
valor1 = int(input("coloque o  primeiro valor : "))
valor2 = int(input("coloque o segundo valor : "))

#verificar se são diferentes
if valor1 != valor2 :
    valor3 = int(input("coloque o terceiro  valor : "))
    if valor3 != valor1 and valor3 != valor2:
        valores = valor1,valor2,valor3
        listvalores= list(valores)   #colocando os valores em uma lista
        crescente = sorted(listvalores)   #colocando os valores em ordem crescente
        decrescente = sorted(listvalores,reverse=True)  #colocando os valores em ordem decrescente

        print("os valores em ordem crescente",crescente)
        print("os valores em ordem decrecente",decrescente)
 #revertendo valores list converte os valores para lista, e reversed inverte para decrescente
    else:
        print("O terceiro numero deve ser diferente dos primeiros numeros ")
  
else:

        print("os valores sao  iguais :", valor1 ,valor2)

#verificar ordem crescente e decrescente







    




  












       




 

    
        





        

         
        

    
