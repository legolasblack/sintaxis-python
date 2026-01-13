age = 25 
license = True

if age >= 18 and license:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")    
    
    """ imprecion final del codigo
-----------------------------------
Puedes conducir.
"""

#Ejemplo 2 uso del operador or
temperature = 30   
is_raining = False
if temperature > 25 or is_raining:
    print("El clima es adecuado para salir.")
else:
    print("Mejor quedarse en casa.")
    
    """ imprecion final del codigo
-----------------------------------
El clima es adecuado para salir.
"""

#Ejemplo 3 uso del operador not
is_hungry = False
if not is_hungry:
    print("No tengo hambre.")
else:
    print("Tengo hambre.")
    
    """ imprecion final del codigo
-----------------------------------
No tengo hambre.
"""

#Ejemplo 4 short Ciscuiting
name = "Alice"
print(name and "El nombre es " + name.upper())

""" imprecion final del codigo
-----------------------------------
El nombre es ALICE
""" 