def sumar_dos():
    a = input("numero 1: ")
    b = input("numero 2: ")
    while True:
        try:
             resultado = int(a) + int(b)
        except:
             print("Poar favor, no te detegnas")
             
    return resultado


print(sumar_dos())
