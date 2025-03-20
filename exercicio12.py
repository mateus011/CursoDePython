# crianção de uma lista 
def inserir_numlist():
    numeros =  [1,2,3,4,5,6,7,8,9] #tabela type list
    num = int(input('coloque um numero na lista: ')) #pegando numero do usuario
    numeros.append(num) # função para colocar o  numero no final da lista 
    print(f'{numeros}, é o numero insirido é {num}')# imprimir na tela
     

def remove_numlist():
    numeros =  [1,2,3,4,5,6,7,8,9] #tabela type list
    num = int(input('coloque o numero que deseja apagar: '))
    numeros.remove(num)
    print(f'{numeros}, é o numero que foi removido da lista foi o {num}')

def organizar_alfabetica():
    nomes = ['mateus','jason','clayde','vasconselo','aride','letes']
    nomes.sort()
    print(f'{nomes}')

