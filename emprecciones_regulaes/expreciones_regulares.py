import re 

texto = '''Hola maestro como  mi primer linia?
esta es la segunda linia
esta es la ultima linia '''

#Haciendo una busqueda simple
resultado = re.findall("esta",texto)



print(resultado)