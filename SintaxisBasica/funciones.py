#definiremos la sintaxis de una funcion
#primero se utiliza la palabra reservada def seguido por el nombre de la funcion los parantesis y dos puntos para finalizar
#se deve gerarquizar con indentacion las lineas pertenecientes a la funcion 

#en esta primera funcion se redacta la sintaxis donde no se le mandan parametros o argumentos a la funcion
def printMesagge():
    print("hola desde un mensaje")

#En esta funcion mandamos un primer parametro donde se utiliza el pase de parametros para intyectar la funcion con un mensaje personalizado
def printMesaggeCustom(Msj):
    print(Msj)

#ahora vamos a definir una funcion donde utilice varios parametros y que regrece el resultado
def Suma(num1, num2):
    num3 = num1 + num2 
    return num3 

printMesagge()
printMesaggeCustom("hola esto es un mensaje presonalizado")
print(Suma(5, 12))

