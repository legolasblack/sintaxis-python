is_new_dev = False
knowns_python = True
interested_in_django = True


if is_new_dev:
    print("Bienvenido al mundo de la programacion")
if knowns_python:
    print("Puedes continuar con Django")
elif interested_in_django:
    print("Puedes aprender Django") 
else:
    print("Debes aprender Python primero")
#Salida esperada
#Puedes continuar con el Django 

""" imprecion final del codigo
-----------------------------------
Puedes continuar con Django
"""     

#Ejemplo 2 declariacion anidad de ifs

edad = 20
tiene_entrada = True

if edad >= 18:
    print("Eres mayor de edad.")

    if tiene_entrada:
        print("Puedes entrar al evento.")
    else:
        print("No puedes entrar porque no tienes entrada.")

else:
    print("Eres menor de edad.")

    if tiene_entrada:
        print("Tienes entrada, pero no puedes entrar por ser menor.")
    else:
        print("No tienes entrada y además eres menor.")

""" imprecion final del codigo
-----------------------------------
Eres mayor de edad.
Puedes entrar al evento.
"""