def es_primo(num):
    # Verifica si el número es menor que 2, en cuyo caso no es primo
    if num < 2:
        return False
    
    # Itera sobre los números desde 2 hasta num - 1 para verificar si es divisible
    for i in range(2, num):
        if num % i == 0:
            return False
    
    # Si no se encontraron divisores, el número es primo
    return True

def primo_hasta(num):
    primos = []
    
    # Itera sobre los números desde 2 hasta el número proporcionado (incluido)
    for i in range(2, num + 1):
        # Verifica si el número i es primo usando la función es_primo
        if es_primo(i):
            primos.append(i)
    
    return primos 

# Llama a la función primo_hasta con el argumento 13
resultado = primo_hasta(13)

# Imprime el resultado
print(resultado)
