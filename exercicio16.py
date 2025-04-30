# estudando função lambda

def soma(x):
    resultadoElevado = lambda x: x + 20   
    return resultadoElevado(x) ** 2 

# print(soma(20))

lambda x: x + 10   # usado dentro de uma função 
                   #x: expressoens como variaveis 
                   # a partir do dois pontos  e a expressão.
                   # colocada dentro de uma variavel 


x = lambda a, b : a * b  # função lambda usando dois argumentos
print(x(5, 6))
