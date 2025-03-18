# concatenando listas

def jutando_listas():
    numeros = [1,2,3,4,5,6,7,8,9]
    letras = ['a','b','c','d','e','f','g','h','i']
    numeros.extend(letras)
    print(numeros)

def loop_list():
    numeros = [10,20,30,60,70,90,140] # lista
    for i in numeros: #repetição dentro da lista
        print(f'Os numeros da lista são {i}') # printando os numeros pelo index ,index= elemento


def verificacao_cores():
    cores = ['azul','vermelho','laranja','preto']
    cor = input('cor que deseja verificar:')
    if  cor.lower() in cores:  #lower coloca as letras em minuscula 
        print(f'há esta cor no estoque')
    else:
        print(f'cor nao encontrada em estoque')



def juntando_listas_zip():
    numeros = [1,2,3,4,5,6]
    letras = ['a','b','c','d','e','f']

    lista_final = zip(letras,numeros)  #juntando listas
    # print(lista_final) # se nao for trasformado em lista aparecera este resultado zip object at 0x00000278A546EB40
    print(list(lista_final))


def criacao_lista():
    valor_usuario = input('digite os valores com virgula:')
    lista_final = valor_usuario.split(', ')
    print(lista_final)

