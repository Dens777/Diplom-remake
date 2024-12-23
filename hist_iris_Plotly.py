import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Загружаем датасет Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=columns)


fig = px.histogram(iris, x='sepal_length', color='species', barmode='overlay', title='Гистограмма длины чашелистика (Sepal Length) - Plotly',
                   labels={'sepal_length': 'Длина чашелистика (cm)', 'count': 'Частота'})
# barmode='overlay' — режим наложения групп гистограммы,
# при котором они будут накладываться друг на друга;
# barmode - аргумент, который позволяет указать режим диаграммы
# labels — метки для осей

fig.update_layout(xaxis_title='Длина чашелистика (cm)', yaxis_title='Частота')
# метод для настройки меток и заголовков на графике
fig.show()
