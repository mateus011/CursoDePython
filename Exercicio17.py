# usando map e lambda 

lista = [100,200,300,400,500]

# def div(x):
#   expo = lambda x: x *10
#   return expo(x)/10 

# listaM = map(div,lista)
# print(list(listaM))

# transformar em lamnba e map em uma linha 
print(list(map(lambda x: x * 10/10,lista)))

