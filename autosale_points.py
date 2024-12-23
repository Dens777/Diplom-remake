import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


url = "C:/UrbanUniversity/autosales.csv"
crossings = pd.read_csv(url)
(
sns.scatterplot(
    data=crossings, x="Date_of_sale", y="Global_Sales"
     )
.set(
    title="Объем продаж по годам",
    xlabel="Год",
    ylabel="Объем продаж, тыс.шт",
     )
)

plt.show()