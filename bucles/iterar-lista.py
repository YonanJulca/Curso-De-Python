animales= ["gato","perro","loro","cocodrilo"]
numeros = {73,23,63}
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#recorreindo la lista nuemros y multiplicado cada valor por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)
#forma correcta de intererar
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usado el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else: 
    print("el bucle termino")