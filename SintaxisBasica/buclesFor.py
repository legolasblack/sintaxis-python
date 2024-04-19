#definiremos la sintaxis necesariza para la estructura de control for y for each

for i in [1,2,3]:
    print('hola' + ' indice: '+ str(i) )

#tambien podriamos definir un arreglo y hacer un recorrido por cada parte del arreglo
#esto viene a ser lo mismo que un for each de otros lenguajes de programacion
listMonth = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
for month in listMonth:
    print('mes: '+ month)


#se puede utilizar imprecion por cada elemento de un string bucles for ejemplo:
#haremos una verificacion de email, va a recorrer todo el string y en cuanto encuentre un arroba
#lo volvera true al validador y pasara el if 
email = 'legolas.black.ds@gmail.com'
emailvalidator =  False

for letra in email:
    if(letra == '@'):
        emailvalidator = True

if emailvalidator== True:
    print('es un email valido al contener @')
else:
    print('el email no es valido')


#podemos hacer for con ranges:
for i in range(5):
    print('hola mundo')

#podemos hacer for con ranges:
vueltas= 10
for i in range(vueltas):
    print('hola mundo '+  str(i+1))
    