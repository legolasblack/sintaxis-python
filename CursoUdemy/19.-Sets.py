# SETS (CONJUNTOS) EN PYTHON
"""
Module: Sets (Conjuntos) en Python

Este módulo demuestra el uso completo de sets en Python, incluyendo:

1. CREAR SETS:
    - Creación de sets con llaves {} o función set()
    - Sets vacíos
    - Conversión de listas a sets para eliminar duplicados

2. OPERACIONES BÁSICAS:
    - add(): Agregar un elemento individual
    - update(): Agregar múltiples elementos
    - discard(): Eliminar un elemento específico
    - pop(): Eliminar y retornar un elemento aleatorio

3. OPERACIONES DE CONJUNTOS (Set Operations):
    - Unión (|): Todos los elementos de ambos sets
    - Intersección (&): Elementos comunes
    - Diferencia (-): Elementos en el primer set pero no en el segundo
    - Diferencia simétrica (^): Elementos que están en uno u otro, pero no en ambos

4. MÉTODOS ÚTILES:
    - len(): Obtener la cantidad de elementos
    - in: Verificar pertenencia
    - copy(): Crear una copia del set
    - clear(): Vaciar el set

5. CASOS DE USO PRÁCTICOS:
    - Eliminar duplicados de listas
    - Encontrar elementos comunes entre colecciones
    - Operaciones matemáticas de conjuntos

Características de los Sets:
- Desordenados: No mantienen un orden específico
- Sin duplicados: Automáticamente elimina elementos repetidos
- Mutables: Se pueden modificar después de su creación
- No indexables: No se accede mediante índices
"""
# Un set es una colección desordenada, sin duplicados y mutable
# Se define con llaves {} o la función set()

# 1. CREAR SETS
print("=== CREAR SETS ===")
set1 = {1, 2, 3, 4, 5}
print(f"Set: {set1}")

# Set vacío (usar set(), no {})
conjunto_vacio = set()
print(f"Set vacío: {conjunto_vacio}")

# Set desde una lista (elimina duplicados automáticamente)
conjunto2 = set([1, 2, 2, 3, 3, 3])
print(f"Set desde lista con duplicados: {conjunto2}")

# 2. OPERACIONES BÁSICAS
print("\n=== OPERACIONES BÁSICAS ===")
# Agregar un elemento
set1.add(6)
print(f"Después de add(6): {set1}")

# Agregar múltiples elementos
set1.update([7, 8, 9])
print(f"Después de update([7,8,9]): {set1}")

# Eliminar un elemento
set1.discard(5)
print(f"Después de discard(5): {set1}")

# Eliminar y retornar un elemento aleatorio
elemento = set1.pop()
print(f"Pop retornó: {elemento}, Set: {set1}")

# 3. OPERACIONES DE CONJUNTOS
print("\n=== OPERACIONES DE CONJUNTOS ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unión
union = a | b
print(f"Unión {a} | {b} = {union}")

# Intersección
interseccion = a & b
print(f"Intersección {a} & {b} = {interseccion}")

# Diferencia
diferencia = a - b
print(f"Diferencia {a} - {b} = {diferencia}")

# Diferencia simétrica
diferencia_simetrica = a ^ b
print(f"Diferencia simétrica {a} ^ {b} = {diferencia_simetrica}")

# 4. MÉTODOS ÚTILES
print("\n=== MÉTODOS ÚTILES ===")
conjunto3 = {1, 2, 3}
print(f"Longitud: {len(conjunto3)}")
print(f"¿2 está en el set?: {2 in conjunto3}")
print(f"¿5 está en el set?: {5 in conjunto3}")

# Copiar set
conjunto4 = conjunto3.copy()
print(f"Copia: {conjunto4}")

# Limpiar set
conjunto_temp = {1, 2, 3}
conjunto_temp.clear()
print(f"Set después de clear(): {conjunto_temp}")

# 5. CASOS DE USO
print("\n=== CASOS DE USO ===")
# Eliminar duplicados
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista sin duplicados: {sin_duplicados}")

# Verificar elementos comunes
usuarios_activos = {"juan", "maria", "carlos", "ana"}
usuarios_premium = {"maria", "ana", "luis"}
usuarios_comunes = usuarios_activos & usuarios_premium
print(f"Usuarios que son activos Y premium: {usuarios_comunes}")