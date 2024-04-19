# En este tutorial definiremos listas y arreglos pasando por sus diferente formas y trucos para manipularlas


list =[5,4,3,2,1];

listStr=['diego','Maria','Nayeli','Gaby','Dahlia']

#se genera dos array o listas las cuales procederemos a imprimirlas una de enteros y una de strings

print(list)
print(listStr[0])

#tambien podemos acceder a rangos en especficico de la lista 

listRecortada= listStr[0:3]

print(listRecortada)

#para agregar elementos nuevos al arreglo utilizaremos la funcion append
#esta funcion solo nos ayuda a insertar elemntos al final de la fila 

listRecortada.append("Albatroz")
listRecortada.append("Pelicanos")
listRecortada.append(23)
listRecortada.append(True)

print(listRecortada)

#si lo que queremos es insertar elmentos en una posicion especifica del arreglo 
#utilizaremos la funcion insert

listRecortada.insert(2, "Astronotus Ocellatus")

print(listRecortada)


#si quiero encontrar un elemento en la lista y que nos retorne el indice donde se encuentra 
#lo puedes encontrar por el contenido del elemento y retrona el indice donde se encuentra el elemento 

print("indice de palabra buscada",  listRecortada.index("Astronotus Ocellatus"))


#tambien podemos verificar si una palabra es contenida por el arreglo con la siguiente exprecion 

print("Albatroz" in listRecortada)

#con el elemnto extend se puede concatenar dos listas

newList= [1,2,3]

newList.extend(listRecortada)

print(newList)

#a su vez tambien podemos borras posiciones en especifico del arreglo 

newList.remove('Pelicanos')

print(newList)
print(len(newList))



