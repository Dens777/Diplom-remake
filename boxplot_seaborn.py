import seaborn as sns
import matplotlib.pyplot as plt

# загружаем дата
tips = sns.load_dataset("tips")
# строим Boxplot-график
sns.boxplot(x="day", y="total_bill", data=tips)

plt.show()

# Boxplot-графики используются для визуализации сводной статистики данных.
# Они показывают важные числа, такие как медиана, максимум, минимум и выбросы