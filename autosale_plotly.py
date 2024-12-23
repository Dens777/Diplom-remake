import pandas as pd
import plotly.express as px


url = "C:/UrbanUniversity/autosales.csv"
vg_data = pd.read_csv(url)
dinamic_by_region = vg_data[
        ['LADA', 'KIA', 'HYUNDAI', 'HAVAL', 'CHERY', 'Date_of_sale']
    ].groupby('Date_of_sale').sum()

# линейный график
fig = px.line(vg_data, x='Date_of_sale', y='Global_Sales', title='Суммарный объём продаж автомобилей',
                labels={'Date_of_sale': 'Год выпуска', 'Global_Sales': 'Автомобилей, тыс.ед'}).update_layout(font_size=15)
# update_layout(font_size=15) установление размера шрифта для какого-либо элемента макета
# графика, например, заголовка или меток осей.

# настраиваем заголовки осей
fig.update_layout(xaxis_title='Год', yaxis_title='Автомобилей, тыс.ед')


fig.show()