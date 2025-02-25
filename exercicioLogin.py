# exercicio de login
# variaveis 
AdminUsername = 'admin'
AdminPassword = 123456
# entrada de dados
Username = input('Coloque aqui seu username :')
Password = int(input('coloque sua senha aqui: '))
#verificar se no sistema ja existe este usuario
if Username == AdminUsername and Password == AdminPassword:
    print('Login OK')
else:
    print('Usuario ou senha incorreta')





