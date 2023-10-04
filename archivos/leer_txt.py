
#usuando un open para aprbir un archivo con una codificacion de utf-8
archivo_sin_leer = open("archivos//yonan.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linia por linea
linea_1 = archivo_sin_leer.readline()

print(linea_1)