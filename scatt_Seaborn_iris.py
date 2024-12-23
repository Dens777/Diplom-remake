import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Подключаемся к датасет iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# данные Dataset (длина и ширина наружной и внутренней доли околоцветника)
# и вид ирисов
iris = pd.read_csv(url, header=None, names=columns)

df = sns.load_dataset('iris')


# визуализация с помощью pairplot
sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=50, edgecolor="black", linewidth=2.5))
# kind="scatter" - построится точечная диаграмма,
# hue - разделение точек на группы будет происходить переменной «species»
# plot_kws= - настройка параметров парного графика
# pairplot, s=80 - размер маркера,
# edgecolor - цвет границ "белый",
# linewidth - ширина линии
plt.show()
