
def require_auth(funcion):
    def wrapper(*args, **kwargs):
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        if usuario == "admin" and password == "secreto":
            return funcion(*args, **kwargs)
        else:
            print("Autenticación fallida")
    return wrapper

@require_auth
def funcion_protegida():
    print("Acceso concedido a la función protegida")
funcion_protegida() 