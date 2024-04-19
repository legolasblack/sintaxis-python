#vamos a expresar l sintaxis correcta del bucle while

i = 1 

while i <=10:
    print('hello word '+ str(i))
    i=i+1

#se utiliza la pabra break para cortar el flujo del ciclo


intentos=0
while intentos<=3:
    print('Introduce tu password')
    passWord = input()
    if passWord == 'legolas':
        print('ya estas logeado')
        break
    else:
        print('la contaseña es incorrecta')
        intentos = intentos + 1
        
if intentos >=3 :
    print ('alcanzaste el numero maximo de intentos')



