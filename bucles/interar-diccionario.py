diccionario = {
    "nombre": "yonan",
    "apellido": "julca",
    "subs": 10000
}

#recorriendo con formas de key y value 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")