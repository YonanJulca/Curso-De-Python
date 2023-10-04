import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_grafico\\pedos.csv")

sns.lineplot(x="fecha",y="pedos",data=df)


plt.show()