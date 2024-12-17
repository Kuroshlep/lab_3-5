import pandas as pd

# Загрузка данных
data = pd.read_csv('athlete_events (4).csv')

# Шаг 1: Количество значений в каждом признаке и отсутствие данных
print("Количество значений в каждом признаке:")
print(data.count())
missing_data = data.isna().sum()
print("\nКоличество отсутствующих данных в каждом признаке:")
print(missing_data)

most_missing = missing_data.idxmax()
print(f"\nПризнак с наибольшим количеством отсутствующих данных: {most_missing} ({missing_data[most_missing]} пропусков)")

# Шаг 2: Статистическая информация
print("\nСтатистическая информация (возраст, рост, вес):")
print(data[['Age', 'Height', 'Weight']].describe())

# Шаг 3: Самый молодой участник в 1992 году
youngest_1992 = data[(data['Year'] == 1992) & (data['Age'].notna())].sort_values('Age').iloc[0]
print(f"\nСамый молодой участник в 1992 году: {youngest_1992['Name']}, возраст: {youngest_1992['Age']}, дисциплина: {youngest_1992['Event']}")

# Шаг 4: Список всех видов спорта
sports = data['Sport'].drop_duplicates().sort_values()
print("\nСписок всех видов спорта:")
print(sports.tolist())

# Шаг 5: Средний рост теннисисток на ОИ 2000 года
female_tennis_2000 = data[(data['Year'] == 2000) & (data['Sex'] == 'F') & (data['Sport'] == 'Tennis')]
avg_height_tennis_2000 = female_tennis_2000['Height'].mean()
print(f"\nСредний рост теннисисток на ОИ 2000 года: {avg_height_tennis_2000:.2f} см")

# Шаг 6: Золотые медали Китая в настольном теннисе на ОИ 2008 года
china_table_tennis_2008 = data[(data['Year'] == 2008) & (data['Team'] == 'China') & (data['Sport'] == 'Table Tennis') & (data['Medal'] == 'Gold')]
gold_medals_china = china_table_tennis_2008.shape[0]
print(f"\nКоличество золотых медалей Китая в настольном теннисе на ОИ 2008 года: {gold_medals_china}")

# Шаг 7: Изменение количества видов спорта на летних ОИ в 2004 и 1988 годах
sports_2004 = data[(data['Year'] == 2004) & (data['Season'] == 'Summer')]['Sport'].nunique()
sports_1988 = data[(data['Year'] == 1988) & (data['Season'] == 'Summer')]['Sport'].nunique()
print(f"\nКоличество видов спорта на летних ОИ 2004 года: {sports_2004}")
print(f"Количество видов спорта на летних ОИ 1988 года: {sports_1988}")
print(f"Изменение количества видов спорта: {sports_2004 - sports_1988}")

# Шаг 8: Гистограмма возраста мужчин-керлингистов на ОИ 2014 года
import matplotlib.pyplot as plt

curling_men_2014 = data[(data['Year'] == 2014) & (data['Sport'] == 'Curling') & (data['Sex'] == 'M')]
curling_men_2014['Age'].hist(bins=10)
plt.title("Распределение возраста мужчин-керлингистов (ОИ 2014)")
plt.xlabel("Возраст")
plt.ylabel("Частота")
plt.show()

# Шаг 9: Количество медалей и средний возраст спортсменов на зимней ОИ 2006 года
winter_2006 = data[(data['Year'] == 2006) & (data['Season'] == 'Winter') & (data['Medal'].notna())]
medals_by_country = winter_2006.groupby('NOC').agg(
    medals=('Medal', 'count'),
    avg_age=('Age', 'mean')
).query('medals > 0')
print("\nКоличество медалей и средний возраст спортсменов на зимней ОИ 2006 года:")
print(medals_by_country)

# Шаг 10: Сводная таблица медалей по странам и их типу на зимней ОИ 2006 года
pivot_table_medals = winter_2006.pivot_table(
    index='NOC',
    columns='Medal',
    values='ID',
    aggfunc='count',
    fill_value=0
)
print("\nСводная таблица медалей на зимней ОИ 2006 года:")
print(pivot_table_medals)
