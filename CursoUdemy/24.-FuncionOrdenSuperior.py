#se define una funcion de orden superior que verifica la autenticacion de un usuario antes de permitir el acceso a una funcion dada
#Esta funciona como como en ejecutor de toma de desicion si se ejecuta algo o no dependiendo de la autenticacion
#Se declara una funcion principal la cual contendra un wrapper que hara la verificacion de usuario
#Si el usuario es correcto se ejecuta la funcion pasada como argumento, de lo contrario se deniega el acceso

def require_auth(funcion):
   def envoltorio(user):
       if user == "admin":
           return funcion(user)
       else:
           print("Acceso denegado")
           
   return envoltorio
    
#Aqui esta la definicion de la funcion que sera protegida por la funcion de orden superior
def admin_dashboard(user):
    print(f"Bienvenido al panel de administración, {user}")
    

#Aqui se iguala la funcion protegida a la funcion de orden superior
#lo cual te permite o retornar la ejecucion de la funcion protegida o denegar el acceso
#auth_dashboard es ahora una la funcion envoltorio que verifica la autenticacion antes de llamar a admin_dashboard
#y por medio de ella puede recibir los parametros definidos y utiliados por envoltorio
auth_dashboard = require_auth(admin_dashboard)

#aqui solo se llama a la funcion auth_dashboard la cual maneja la autenticacion y la llamada a admin_dashboard
while True:
    usuario = input("Ingrese su nombre de usuario: ")
    auth_dashboard(usuario)