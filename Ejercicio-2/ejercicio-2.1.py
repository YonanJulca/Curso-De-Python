
def obtener_compañero(cantidad_de_compañero):
    compañeros = []
    for i in range(cantidad_de_compañero):
        nombre = input("Ingrese el nombre del compañero")
        edad = int(input("ingrese la edad del compañero"))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañero(5)

print(f"El profesor es: {profesor} y su asistente es {asistente}")



    

    
    
    
