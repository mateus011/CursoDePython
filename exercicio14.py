# trabalhando com arrays
from array import array  # inportando o modulo
letras = ['a','b','c','d','e','f']

numeros_inteiros = [1,2,3,4,5,6]
numeros_Flutuantes = [1.5,1.8,1.6,2.0]

letras = array('u',['a','b','c','d','e','f']) # trasformando a lista array , o 'u' significa string
numeros_inteiros = array('i',[1,2,3,4,5,6]) # trasformando a lista de inteiros em array , 'i' = inteiros
numeros_Flutuantes = array('f',[1.5,1.8,1.6,2.0]) # trasformando a lista de float em  array , 'f' = float


print(letras)
print(numeros_inteiros)
print(numeros_Flutuantes)
