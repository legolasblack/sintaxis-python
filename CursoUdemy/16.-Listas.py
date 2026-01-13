list_numbers = [1, 2, 3, 4, 5]
list_strings = ["apple", "banana", "cherry"]
list_mixed = [1, "hello", True, 3.14]

shopping_cart = [] 

shopping_cart.append("laptop")
shopping_cart.append("mouse")
shopping_cart.append("keyboard")    
print("Carrito de compras:", shopping_cart)
#Salida esperada
#Carrito de compras: ['laptop', 'mouse', 'keyboard']   


#metodos de listas

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Agrega "orange" al final de la lista
print("Después de append:", fruits)
#Salida esperada
#Después de append: ['apple', 'banana', 'cherry', 'orange']

fruits.remove("banana")  # Elimina "banana" de la lista
print("Después de remove:", fruits)
#Salida esperada
#Después de remove: ['apple', 'cherry', 'orange']
fruits.insert(1, "blueberry")  # Inserta "blueberry" en el índice 1
print("Después de insert:", fruits)
#Salida esperada
#Después de insert: ['apple', 'blueberry', 'cherry', 'orange']
fruits.pop()  # Elimina el último elemento de la lista
print("Después de pop:", fruits)
#Salida esperada
#Después de pop: ['apple', 'blueberry', 'cherry']
fruits.sort()  # Ordena la lista en orden alfabético
print("Después de sort:", fruits)
#Salida esperada
#Después de sort: ['apple', 'blueberry', 'cherry']
fruits.reverse()  # Invierte el orden de la lista
print("Después de reverse:", fruits)
#Salida esperada
#Después de reverse: ['cherry', 'blueberry', 'apple']
#Accediendo a elementos de una lista
numbers = [10, 20, 30, 40, 50]
print("Primer elemento:", numbers[0])  # Accede al primer elemento
#Salida esperada
#Primer elemento: 10
print("Último elemento:", numbers[-1])  # Accede al último elemento
#Salida esperada
#Último elemento: 50
print("Elementos del índice 1 al 3:", numbers[1:4])
# Accede a una porción de la lista
#Salida esperada
#Elementos del índice 1 al 3: [20, 30, 40