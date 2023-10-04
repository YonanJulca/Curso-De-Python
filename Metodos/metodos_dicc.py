diccionario = {
    "nombre" : "yonan",
    "apellido" : "julca",
    "subs" : 1000
}

#nos devuelve n objeto diccionario
clave = diccionario.keys()

#obteniendo un elemento con un get()  y si no encuentra nada el proyecto continua
clave = diccionario.get("apellido")

#aliminando todo del diccionario
#diccionario.clear()

#eliminado un elemento un diccionario
diccionario.pop("nombre")



#impreme
print(diccionario)