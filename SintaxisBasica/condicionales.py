#Condicionales
#--if, es importante al terminar de definir el if utilizar los dos puntos


def evaluacion(nota):
    valoracion="aprovado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print("Introduce tu calificacion")
minota=input()
print(evaluacion(int(minota)))


#procedermos a definir un if con else y con elseif 

def evaluacion2(key):
    if key == True:
        print("todo fue cierto")
    else:
        print ("nada fue cierto")

myKey=input();

evaluacion2(bool(myKey))

#prcedemos a crear la sintaxis para una estructura else if

def evaluacionElseIf(num):
    if num < 0 :
        print('El numero es un numero negativo')
    elif num == 0:
        print('El numero es cero')
    elif num > 0:
        print('El numero es positivo')

print('elige un numero para saber si es negativo o positivo:')
numexemple=input()
evaluacionElseIf(int(numexemple))

#para evitar el uso de and y or podemos concatenar nuestros
# operadores dentro de la misma expresion, se demuestra en el ejemplo siguiente 
#dentro de la exprecion if

def evaluacionCondicionConcatena(num):
    if 0<=num<=100 :
        print('Tu numero se encuentra entre el 0 y 100, incluidos los anteriores')
    else:
        print('el numero esta fuera de rango permitido')

print('elige un numero:')
numexemple=input()
evaluacionCondicionConcatena(int(numexemple))


#operadores and y or 
kilometros = 50 
hermanos = 3
salario = 2000


if kilometros < 100 and hermanos >= 4 and salario < 5000:
    print('si te alcanza el dinero')
else:
    print('no te alcanza el dinero')

if kilometros >25 and 0 < hermanos < 4 or salario >10000:
    print('el salario si te alcanza')
else:
    print('no te alcanza para nada') 
