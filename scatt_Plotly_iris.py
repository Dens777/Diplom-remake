import plotly.express as px

data = px.data.iris()
# построение диаграммы рассеяния
fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species")

fig.show()