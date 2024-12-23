import pandas as pd
from matplotlib.pyplot import pie, show

url = "C:/UrbanUniversity/autosales.csv"
df = pd.read_csv (url)


sums = df.groupby(df['Date_of_sale'])['KIA'].sum()

pie(sums, labels=sums.index,);
show()

sums = df.groupby(df['Date_of_sale'])['HAVAL'].sum()

pie(sums, labels=sums.index,);
show()