dados = input("digite seu nome , sua idade e altura : ").split() #split divide o texto com espaços
nome = dados[0].upper() # ira receber da variavel dados o nome no index 0 , upper() faz com que fique todo em Maiuscula
idade = dados[1] # ira receber a idade que esta no index 1
altura = dados[2]
print(f"Meu nome é {nome} , tenho {idade} anos de idade, e minha é minha é de  {altura} ")

 