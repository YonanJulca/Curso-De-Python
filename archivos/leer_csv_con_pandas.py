import pandas as pd
#usuando la funcion read_csv para leer arcchivo csv
df = pd.read_csv("archivos//datos.csv",)

#obteniendo los datos de la columna nombre
nombre = df["nombre"]

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")

print(df_ordenado)

