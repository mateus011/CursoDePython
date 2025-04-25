# aprendendo sobre dicionarios 
def dicionario():
    aluno = {'nome': 'ana','idade': 16,'nota': 'A','Aprovação': True}
# para chamar um index , utilizar as keys
    print(aluno['nome'])

# dicionario()

def modificandoDicionario():
    aluno = {'nome': 'ana','idade': 16,'nota': 'A','Aprovação': True}
    aluno.update({'nome': 'José','idade': 18,'nota': 'b','Aprovação': True})
# também  podemos usar o .get, para buscar informação, e se não existir ela mostra a mensagem 
    print(aluno.get('endereco','nâo existe'))
    # print(aluno)    

# modificandoDicionario()

def remoçãoValor():
    aluno = {'nome': 'ana','idade': 16,'nota': 'A','Aprovação': True}
    del aluno['idade']
    print(aluno)

# remoçãoValor()

def loopDicionarios():
    aluno = {'nome': 'ana','idade': 16,'nota': 'A','Aprovação': True}

    # for x in aluno:
    #     print(x)
        # desta forma so ira inprimir as keys

    # for i in aluno.values():
    #  print(i)
    #  mostrara apenas os valores

    # for i in aluno.items():
    #     print(i)
        #  mostrara todos os itens em forma de tupla
    for Keys, Values in aluno.items():
       print(Keys,Values)

# tirou da tupla para as variaveis Keys e values 

loopDicionarios()