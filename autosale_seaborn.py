import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "C:/UrbanUniversity/autosales.csv"
vg_data = pd.read_csv(url)

dinamic_by_region = vg_data[
        ['LADA', 'KIA', 'HYUNDAI', 'HAVAL', 'CHERY', 'Date_of_sale']
    ].groupby('Date_of_sale').sum()

sns.set_theme(style="darkgrid")  #устанавливается темная сетка фона

# создание линейного графика с помощью функции lineplot
fig = plt.figure(figsize=(12, 6)) # устанавливаем размер фигуры в дюймах (ширина, высота)
lineplot = sns.lineplot(data=dinamic_by_region)
lineplot.set_title('Объем продаж автомобилей по производителям за год', fontsize=16)
lineplot.set_xlabel('Год')
lineplot.set_ylabel('Автомобилей, тыс.шт')

plt.show()

