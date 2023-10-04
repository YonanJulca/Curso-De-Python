#creando una lista con list()
lista = list(["hola","yonan",34,56,57,True])

#de vuelve la cantidad de elementos de la lista
cantidad_elemento = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJAA")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"Toma cafe")

#agregando varios elementos a la lsita 
lista.extend([False,2030])

#eliminado un elemento de una lista 
lista.pop(-3)

#removinendo un elemento por su valor
lista.remove("hola")

#eliminando todos los elementos de la lista 
#lista.clear()

print(lista)