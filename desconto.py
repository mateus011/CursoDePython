valor_compra = float(input('Coloque  o valor da compra : '))
if valor_compra >= 200:
    Valor_desconto = valor_compra - (valor_compra * 0.2) # desconto de 20 por cento 
elif valor_compra >= 100 :
    Valor_desconto = valor_compra - (valor_compra * 0.1)  # desconto de 10 por cento 
else:
    Valor_desconto = valor_compra - (valor_compra * 0.05) # desconto de 5 por cento    

print(f'O valor com desconto é de R$: {Valor_desconto:.2f}')
 