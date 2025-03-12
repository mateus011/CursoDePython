# triangulo com o simbolo @
n = 8
simbol = '@'
for i in range(n):
    for j in range(0,i+1):
        print(f'{simbol}',end=' ')
    print()
for k in range(n):
    for l in range(k,n-1):
         print(f'{simbol}',end=' ')
    print()


