import numpy as np

# Загрузка данных из файлов
countries = np.genfromtxt('lab_3/global-electricity-generation.csv', delimiter=',', skip_header=1, usecols=0, dtype=str)
production = np.genfromtxt('lab_3/global-electricity-generation.csv', delimiter=',', skip_header=1, usecols=range(1, 31))
consumption = np.genfromtxt('lab_3/global-electricity-consumption.csv', delimiter=',', skip_header=1, usecols=range(1, 31))

# Замена NaN на 0
production = np.nan_to_num(production, nan=0)
consumption = np.nan_to_num(consumption, nan=0)

# 2. Построение одномерных массивов среднего за последние 5 лет
avg_production_last5 = np.mean(production[:, -5:], axis=1)  # Среднее производство
avg_consumption_last5 = np.mean(consumption[:, -5:], axis=1)  # Среднее потребление

# 3.1. Суммарное потребление электроэнергии за каждый год
total_consumption_per_year = np.sum(consumption, axis=0)

# 3.2. Максимальное производство электроэнергии одной страной за один год
max_production_per_year = np.nanmax(production)

# 3.3. Список стран, производящих > 500 млрд кВт·ч ежегодно в среднем за последние 5 лет
countries_over_500 = countries[avg_production_last5 > 500]

# 3.4. Топ 10% стран по потреблению электроэнергии в среднем за последние 5 лет
threshold = np.quantile(avg_consumption_last5, 0.9)  # Квантиль 90%
top_10_percent = countries[avg_consumption_last5 > threshold]

# 3.5. Страны, увеличившие производство электроэнергии в 2021 году более чем в 10 раз по сравнению с 1992 годом
growth_10x = countries[production[:, -1] > 10 * production[:, 0]]

# 3.6. Страны, которые потратили > 100 млрд кВт·ч и произвели меньше, чем потратили
total_production = np.sum(production, axis=1)  # Суммарное производство
total_consumption = np.sum(consumption, axis=1)  # Суммарное потребление
high_spenders = countries[(total_consumption > 100) & (total_production < total_consumption)]

# 3.7. Страна с наибольшим потреблением электроэнергии в 2020 году
max_consumption_2020 = np.argmax(consumption[:, -2])  # Предпоследний столбец - 2020 год
country_max_2020 = countries[max_consumption_2020]

# Вывод результатов
print("3.1. Суммарное потребление электроэнергии за каждый год:")
print(total_consumption_per_year)

print("\n3.2. Максимальное производство электроэнергии одной страной за один год:")
print(max_production_per_year)

print("\n3.3. Страны, производящие более 500 млрд кВт·ч ежегодно в среднем за последние 5 лет:")
print(countries_over_500)

print("\n3.4. Топ 10% стран по потреблению электроэнергии в среднем за последние 5 лет:")
print(top_10_percent)

print("\n3.5. Страны, увеличившие производство в 2021 году более чем в 10 раз по сравнению с 1992 годом:")
print(growth_10x)

print("\n3.6. Страны, которые потратили > 100 млрд кВт·ч и произвели меньше, чем потратили:")
print(high_spenders)

print("\n3.7. Страна с наибольшим потреблением электроэнергии в 2020 году:")
print(country_max_2020)
