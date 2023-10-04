# def suma(lista):
    # numeros_sumados = 0
    # for numero in lista:
    #     numeros_sumados= numeros_sumados + numero
    # return numeros_sumados
# resultado = suma([2,3,1,3])

#utlizando el parametro args

def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("yonan",5,5,7,2,5)
print(resultado)