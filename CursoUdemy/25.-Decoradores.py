
#Definimos una funcion de orden superior que verifica la autenticacion de un usuario antes de permitir el acceso a una funcion dada
#la definimos con un envoltorio y se podria modificar el comportamiento del wrapper sin cambiar la funcion original
#Usamos el decorador @ para aplicar la funcion de orden superior a la funcion protegida
def require_auth(funcion):
   def envoltorio(user):
       if user == "admin":
           return funcion(user)
       else:
           print("Acceso denegado")
           
   return envoltorio


#En esta parte del codigo usamos el decorador @ para aplicar la funcion de orden superior a la funcion protegida    
@require_auth
def admin_dashboard(user):
    print(f"Bienvenido al panel de administración, {user}")
    



while True:
    usuario = input("Ingrese su nombre de usuario: ")
    admin_dashboard (usuario)
