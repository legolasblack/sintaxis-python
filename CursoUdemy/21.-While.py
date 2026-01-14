"""
Práctica de bucle While en Python
El bucle while ejecuta un bloque de código mientras una condición sea verdadera.
"""

# Ejemplo 1: Contador simple
print("=== Ejemplo 1: Contador simple ===")
contador = 1
while contador <= 5:
    """
    Mientras contador sea menor o igual a 5,
    imprime el valor y aumenta en 1
    """
    print(f"Contador: {contador}")
    contador += 1

print("\n=== Ejemplo 2: Validación de entrada ===")
# Solicita un número hasta que sea válido
edad = 0
while edad < 1 or edad > 120:
    """
    Repite la solicitud mientras la edad no esté en rango válido
    """
    try:
        edad = int(input("Ingresa tu edad (1-120): "))
        print(f"Has ingresado: {edad}")
    except ValueError:
        print("Debes ingresar un número válido")
        
print(f"Edad registrada: {edad}")

print("\n=== Ejemplo 3: Suma acumulativa ===")
# Suma números hasta que el usuario escriba 'salir'
suma = 0
while True:
    """
    Bucle infinito que se detiene con break cuando el usuario dice 'salir'
    """
    numero_str = input("Ingresa un número (o 'salir' para terminar): ")
    if numero_str.lower() == 'salir':
        break  # Sale del bucle
    numero = int(numero_str)
    suma += numero
    print(f"Suma actual: {suma}")

print(f"Suma final: {suma}")

#while con else
print("\n=== Ejemplo 4: Bucle while con else ===")
n = 1
while n <= 5:
    print(f"Número: {n}")
    n += 1
else:
    print("El bucle ha terminado correctamente.")

            
