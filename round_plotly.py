import plotly.express as px

# используем dataset "Tips"

df = px.data.tips()
# показывает общ. сумму счета за определенный день
fig = px.pie(df, values="total_bill", names="day")



fig.show()

#   total_bill tip   sex    smoker day  time  size
# 0    90,00   1,01   f      no    Sun  diner  2
# 1    10,34   1,66   m      no    Sun  diner  3
# 2    21,01   3,50   m      no    Sun  diner  3
# 3    23,68   3,31   m      no    Sun  diner  2
# 4    24,59   3,61   m      no    Sun  diner  4
