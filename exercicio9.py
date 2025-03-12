# funcçao de varios argumentos
def soma(*numeros):    #sinal '*' faz com que possa colocar varios argumentos
    resultado  = 0
    for i in numeros:
        resultado += i    #pega os numeros que foram colocados na função e soma
    return resultado


x = soma(2,3,5,7)
print(x)
