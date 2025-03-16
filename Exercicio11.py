# fazendo um programa em que é colocado um numero e retorna o numero escrita
#estalação do mudulo pip install num2words no terminal  para baixar a biblioteca 
from num2words import num2words  # inportando 

num = int(input('coloque o numero que deseja: ')) # pedindo o numero para o usuario 
def numero_Extenso(num):
 return num2words(num, lang='pt-BR') # retornando  linguagem, para portugues , é chama a função num2words

print(numero_Extenso(num)) # printa na tela 






