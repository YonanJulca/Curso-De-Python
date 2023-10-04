import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_grafico\\cofla_ingresos.csv")

sns.barplot(x="fuentes",y="ingresos",data=df)

total_ingreso = df['ingresos'].sum()

plt.show()