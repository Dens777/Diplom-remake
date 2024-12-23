import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Загружаем данные из csv файла
url = "C:/UrbanUniversity/autosales.csv"
vg_data = pd.read_csv(url)

# Статистика продаж автомобилей российского производителя,
# Южнокорейских брендов и триумфальное восхождение китайских брендов.
# По оси ординат отложено число проданных дисков автомобилей по производителю
# по оси абсцисс — год статистических данных по продажам.


dinamic_by_region = vg_data[
        ['LADA', 'KIA', 'HYUNDAI', 'HAVAL', 'CHERY', 'Date_of_sale']
    ].groupby('Date_of_sale').sum()

# линейный график matplotlib
fig = plt.figure(figsize=(12, 6)) # создаём объект Figure с заданным размером изображения в дюймах
lineplot = sns.lineplot(data=dinamic_by_region)
lineplot.set_title('Объем продаж автомобилей по производителям за год', fontsize=16) # размер шрифта элемента (pxl)

lineplot.set_xlabel('Год')
lineplot.set_ylabel('Автомобилей, тыс.шт')
plt.grid()
plt.show()
