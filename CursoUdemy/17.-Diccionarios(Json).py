user = {
    "name":"John Doe",
    "age":30,
    "email":"test@hotmail.com",
    "is_active":True,
    "roles":["admin","user"],
    "address":{
        "street":"123 Main St",
        "city":"Anytown",
        "zip":"12345",
    }
}

print("Nombre:", user["name"])
print("Edad:", user["age"])
print("Email:", user["email"])
print("Activo:", user["is_active"])


print(user.values())
print(user.keys())
print(user.items())

#Agregar un nuevo par clave-valor
user["phone"] = "555-1234"
print("Teléfono agregado:", user["phone"]) 

#Modificar un valor existente
user["age"] = 31
print("Edad modificada:", user["age"])      
#Eliminar un par clave-valor
del user["is_active"]
print("Diccionario después de eliminar is_active:", user)
#Salida esperada
#Nombre: John Doe