#2 listas, una con nombre otra apellidos

nombres = ["Yonan", "Sergio","Matias","Juan"]
apellidos = ["Julca","Marta","Mitra","Pipon"]

#Registarr esta informacion en un texto de forma optica

#Registrar esta información en un TXT de forma óptima

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
