frase = input("Decime una frase de calculo cuanto tardarias si tubieras que que decir: ")

palabra_separadas = frase.split("")
cantidad_de_palabras = len(palabra_separadas)
print(f"Dijsite{cantidad_de_palabras} palabras y tardarias{cantidad_de_palabras/2} segundos en decirlo")
print(f"Yonan lo diria en {cantidad_de_palabras *100 //2}")