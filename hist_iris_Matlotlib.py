import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Загружаем датасет iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# Список столбцов данных (длина и ширина наружной  и внутренней доли околоцветника) и вид ирисов
iris = pd.read_csv(url, header=None, names=columns) # чтение CSV-файла с URL-адреса, без
# заголовка и с заданными именами столбцов

#matplotlib
plt.figure(figsize=(10, 6)) # устанавливаем размер фигуры в дюймах (ширина, высота)
for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    plt.hist(subset['sepal_length'], alpha=0.8, bins=15, label=species)

# Для каждого уникального вида в наборе данных iris создаётся
# гистограмма длины чашелистика (sepal_length) с использованием Matplotlib.
# Для этого в цикле for по каждому уникальному виду (species) создаётся поднабор данных
# (subset) по условию iris['species'] == species. Затем для этого поднабора строится
# гистограмма с параметрами alpha=0,8, bins=15 и label=species.
# Таким образом, код позволяет визуализировать распределение длины чашелистика для
# каждого вида в наборе данных iris.
# Для создания гистограмм в Matplotlib используется метод hist, который принимает
# два основных аргумента: x (набор данных для отображения в гистограмме) и
# bins (количество бинов, на которые должна быть разделена гистограмма).


plt.title('Гистограмма длины чашелистика (Sepal Length) - Matplotlib')
plt.xlabel('Длина чашелистика (cm)')
plt.ylabel('Частота')
plt.legend()   # добавление легенды на график
plt.grid(True) # добавление координатной сетки
plt.show()

