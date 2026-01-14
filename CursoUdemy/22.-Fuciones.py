
def hello(greet, name):
    print(f"{greet}, {name}!")
    



#ejemplo de funcion con valores por defecto
def potencia(base, exponente=2):
    return base ** exponente   

#fucion con retorno.
def suma(a, b):
    return a + b   
total = suma(5, 7)
print(f"La suma de 5 y 7 es {total}")

#funcion con multiples retornos
def operaciones(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    return suma, resta, producto

#funcion con args y kwargs
def funcion_args_and_kwargs(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos con nombre:", kwargs)
    


#seccion de llamada a funciones
hello("Hola", "Carlos")
hello("Good morning", "Alice") 

resultado1 = potencia(3)
print(f"3 al cuadrado es {resultado1}") 
resultado2 = potencia(2, 3)
print(f"2 al cubo es {resultado2}")
resultado3 = potencia(5, 4)
print(f"5 a la cuarta es {resultado3}")


s, r, p = operaciones(10, 4)
print(f"Suma: {s}, Resta: {r}, Producto: {p}")

funcion_args_and_kwargs(1, 2, 3, nombre="Juan", edad=30)
funcion_args_and_kwargs("a", "b", clave1="valor1", clave2="valor2")  

