# Ejemplo de uso de un bucle for each para iterar sobre una lista y sumar sus elementos

my_list = [1, 2, 3, 4, 5]
addtion = 0


for number in my_list:
    print(number)
    addtion += number 
    
    
print("La suma de los elementos de la lista es:", addtion)

# Ejemplo de for each sobre una lista de diccionarios de usuarios
usuarios = [
    {"nombre": "Juan", "edad": 25, "email": "juan@example.com"},
    {"nombre": "María", "edad": 30, "email": "maria@example.com"},
    {"nombre": "Carlos", "edad": 35, "email": "carlos@example.com"}
]

for usuario in usuarios:
    print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Email: {usuario['email']}")
    
""" imprecion final del codigo
-----------------------------------
1
2
3
4
5
La suma de los elementos de la lista es: 15
Nombre: Juan, Edad: 25, Email:
"""

for number in list(range(100)):
    print(number)
    
    
    
    #agamos una distincion aqui, existemn dos tipos de bucles for en python
# el bucle for tradicional y el bucle for each
# el bucle for tradicional se utiliza para iterar sobre una secuencia de numeros
# mientras que el bucle for each se utiliza para iterar sobre los elementos de una coleccion como listas, tuplas o diccionarios.
# Ejemplo de bucle for tradicional que es diferente a como se manejaria en java o c#
print("\nBucle for tradicional:")
for i in range(5):
    print(i)
#Salida esperada
#Bucle for tradicional:
#0
#1
#2
#3
#4
# Ejemplo de bucle for each en python
print("\nBucle for each:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#Salida esperada
#Bucle for each:
#apple
#banana
#cherry
# Ejemplo de bucle for each con diccionarios
print("\nBucle for each con diccionarios:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
#Salida esperada
#Bucle for each con diccionarios:
#name: Alice
#age: 30
#city: New York     
# Ejemplo de bucle for each con tuplas
print("\nBucle for each con tuplas:")
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x: {x}, y: {y}")
#Salida esperada
#Bucle for each con tuplas:
#x: 1, y: 2
#x: 3, y: 4
#x: 5, y: 6
# Ejemplo de bucle for each con sets
print("\nBucle for each con sets:")
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)
#Salida esperada
#Bucle for each con sets:
#1
#2
#3
#4
#5
# Ejemplo de bucle for each con cadenas de texto
print("\nBucle for each con cadenas de texto:")
message = "Hello"
for char in message:
    print(char)
#Salida esperada
#Bucle for each con cadenas de texto:
#H
#e
#l
#l
#o
# Ejemplo de bucle for each con rangos
print("\nBucle for each con rangos:")
for number in range(5):
    print(number)
#Salida esperada
#Bucle for each con rangos:
#0
#1
#2
#3
#4
# Ejemplo de bucle for each con listas anidadas
print("\nBucle for each con listas anidadas:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)
#Salida esperada
#Bucle for each con listas anidadas:
#1
#2
#3
#4
#5
#6
#7
#8
#9
# Ejemplo de bucle for each con diccionarios anidados
print("\nBucle for each con diccionarios anidados:")
students = [
    {"name": "Alice", "grades": [85, 90, 95]},
    {"name": "Bob", "grades": [80, 85, 90]},
    {"name": "Charlie", "grades": [75, 80, 85]}
]
for student in students:
    print(f"Student: {student['name']}")
    for grade in student['grades']:
        print(f"Grade: {grade}")
#Salida esperada
#Bucle for each con diccionarios anidados:
#Student: Alice
#Grade: 85
#Grade: 90
#Grade: 95
#Student: Bob
#Grade: 80
#Grade: 85
#Grade: 90
#Student: Charlie
#Grade: 75
#Grade: 80
#Grade: 85
# Ejemplo de bucle for each con conjuntos anidados
print("\nBucle for each con conjuntos anidados:")
set_of_sets = {{1, 2}, {3, 4}, {5, 6}}
for subset in set_of_sets:
    for element in subset:
        print(element)
#Salida esperada
#Bucle for each con conjuntos anidados:
#1
#2
#3
#4
#5
#6
# Ejemplo de bucle for each con cadenas de texto anidadas
print("\nBucle for each con cadenas de texto anidadas:")
sentences = ["Hello World", "Python is great", "Udemy courses"]
for sentence in sentences:
    for char in sentence:
        print(char)
#Salida esperada
#Bucle for each con cadenas de texto anidadas:
#H
#e
#l
#l
#o
# 
#W
#o
#r
#l
#d
#P
#y
#th
#o
#n
# 
#i
#s
# 
#g
#r
#e
#a
#t
#U
#d
#em
#y
# 
#c
#o
#u
#r
#s
#e
#s

# ejemplo de bucle con index, number in enumerate
print("\nBucle for each con índice usando enumerate:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
#Salida esperada
#Bucle for each con índice usando enumerate:
#Index: 0, Color: red
#Index: 1, Color: green
#Index: 2, Color: blue
