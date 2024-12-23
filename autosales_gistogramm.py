import matplotlib.pyplot as plt
import pandas as pd

url = "C:/UrbanUniversity/autosales.csv"
# Загрузка данных из CSV файла
df = pd.read_csv(url)
#df.head()

# Назначение переменным данных из CSV файла
a = df['Date_of_sale']
b = df['LADA']
c = df['KIA']
d = df['HYUNDAI']
e = df['HAVAL']
f = df['CHERY']


# Создание гистограммы
plt.figure(figsize=(10, 8))
plt.bar(a,b)
plt.bar(a,c)
plt.bar(a,d)
plt.bar(a,e)
plt.bar(a,f)
plt.xlabel('Год')
plt.ylabel('Объем продаж автомобилей, тыс.шт')
plt.title('Объем продаж автомобилей по производителям')
plt.legend(['LADA','KIA','HYUNDAI','HAVAL','CHERY'])
plt.show()
