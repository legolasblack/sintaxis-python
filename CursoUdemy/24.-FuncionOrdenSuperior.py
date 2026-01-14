
def require_auth(funcion):
    def wrapper(*args, **kwargs):
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        if usuario == "admin" and password == "secreto":
            return funcion(*args, **kwargs)
        else:
            print("Autenticación fallida")
    return wrapper

def admin_dashboard(user):
    print("Bienvenido al panel de administración") 
    
auth_view_dashboard = require_auth(admin_dashboard("admin"))

auth_view_dashboard("admin")