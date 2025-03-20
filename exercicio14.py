# trabalhando com arrays , é set
from array import array  # inportando o modulo

def trasform_list():
  letras = ['a','b','c','d','e','f']
  numeros_inteiros = [1,2,3,4,5,6]
  numeros_Flutuantes = [1.5,1.8,1.6,2.0]
  letras = array('u',['a','b','c','d','e','f']) # trasformando a lista array , o 'u' significa string
  numeros_inteiros = array('i',[1,2,3,4,5,6]) # trasformando a lista de inteiros em array , 'i' = inteiros
  numeros_Flutuantes = array('f',[1.5,1.8,1.6,2.0]) # trasformando a lista de float em  array , 'f' = float
  print(letras)
  print(numeros_inteiros)
  print(numeros_Flutuantes)

def setlist():
# set listas
 lista1 = [10,20,30,40,50]
 lista2 = [10,20,60,70]
# modificando a lista para set 
 num1 = set(list(lista1)) #set e usado para modificar para set, perdendo o index
 num2 = set(list(lista2))
 print(num1 | num2) # | chamado de unioh , tirando os numeros repetidos
 print(num1 - num2) # diference
 print(num1 ^ num2) #simetric
 print(num1 & num2) # and



def adicionar():
  l1 = {1,2,3,4,5}
  num = int(input('adicione o numero no set: '))
  l1.add(num) # função de adicionar numeros em um setlist
  print(l1)


def updateset():
  l1 = {1,2,3,4,5}
  l1.update({6,7,8,9,10}) #adicionado mais de um numero
  print(l1)


def removeset():
  l1 = {1,2,3,4,5,6,9}
  num = int(input('Coloque o numero de deseja remover: '))
  l1.remove(num)  # remove o  numero da setlist
  print(l1)


