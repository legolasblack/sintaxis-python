#Aprenderemos la sintaxis y como definir Diccionarios
#dentro de los diccionarios de datos no pueden repetirce claves a cada 
#en esta practica aprenderemos a distinguir, crear, modificar, eliminar , 
#basicamente funciona 

diccionario={"Alemania":"Berlin", "Mexico":"cd. Mexico", "España": "Madrid"}
print(diccionario)

# agregamos un elemento al diccionario 
diccionario["Italia"]= "Sicilia"
print(diccionario)

#modificacion de una variable en especifico
diccionario["Italia"]= "Roma"
print(diccionario)

#Eliminar de una variable en especifico
del  diccionario["Italia"]
print(diccionario)


#tambiem podemos acceder a imprimir las llaves y los valores de un diccionario

print(diccionario.keys())
print(diccionario.values())