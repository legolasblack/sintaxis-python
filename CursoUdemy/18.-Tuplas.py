#el concepto de tuplas en python es similar al de las listas, pero con la diferencia clave de que las tuplas son inmutables.
#esto significa que una vez que una tupla es creada, no se pueden modificar sus elementos   
# y no se pueden agregar ni eliminar elementos de una tupla.

my_tupla = (1, 2, 3, 4, 5)
print("Tupla completa:", my_tupla)
#Salida esperada
#Tupla completa: (1, 2, 3, 4, 5
print("Primer elemento:", my_tupla[0])
#Salida esperada
#Primer elemento: 1
print("Último elemento:", my_tupla[-1])
#Salida esperada
#Último elemento: 5
print("Elementos del índice 1 al 3:", my_tupla[1:4])
#Salida esperada
#Elementos del índice 1 al 3: (2, 3, 4) 