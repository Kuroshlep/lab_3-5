import pandas as pd

# Загрузка данных
data = pd.read_csv('telecom_churn.csv')

# Шаг 1: Общая информация о датафрейме
print("Общая информация о данных:")
print(data.info())

# Проверка на отсутствие данных
missing_data = data.isna().sum()
print("\nПропущенные значения в каждом столбце:")
print(missing_data)

# Шаг 2: Количество активных и потерянных клиентов
churn_counts = data['Churn'].value_counts()
churn_percentages = data['Churn'].value_counts(normalize=True) * 100
print("\nКоличество активных и потерянных клиентов:")
print(churn_counts)
print("\nПроцентное соотношение активных и потерянных клиентов:")
print(churn_percentages)

# Шаг 3: Добавление столбца "Средняя продолжительность звонка"
data['Avg_call_duration'] = (
    data[['Total day minutes', 'Total eve minutes', 'Total night minutes']].sum(axis=1) /
    data[['Total day calls', 'Total eve calls', 'Total night calls']].sum(axis=1)
)
sorted_data = data.sort_values('Avg_call_duration', ascending=False)
print("\nТоп-10 клиентов по средней продолжительности звонка:")
print(sorted_data[['Avg_call_duration']].head(10))

# Шаг 4: Средняя продолжительность звонка по категории "Churn"
avg_duration_by_churn = data.groupby('Churn')['Avg_call_duration'].mean()
print("\nСредняя продолжительность звонка по категориям (Churn):")
print(avg_duration_by_churn)

# Шаг 5: Среднее количество звонков в службу поддержки по категории "Churn"
avg_service_calls_by_churn = data.groupby('Churn')['Customer service calls'].mean()
print("\nСреднее количество звонков в службу поддержки по категориям (Churn):")
print(avg_service_calls_by_churn)

# Шаг 6: Таблица сопряженности (Churn и Customer service calls)
import numpy as np

crosstab_calls = pd.crosstab(data['Customer service calls'], data['Churn'])
crosstab_calls_percentage = crosstab_calls.div(crosstab_calls.sum(axis=1), axis=0) * 100
print("\nТаблица сопряженности (Customer service calls и Churn):")
print(crosstab_calls)

# Определение количества звонков, после которого процент оттока выше 40%
high_churn_calls = crosstab_calls_percentage[crosstab_calls_percentage[True] > 40].index.min()
print(f"\nМинимальное количество звонков в службу поддержки, при котором отток выше 40%: {high_churn_calls}")

# Шаг 7: Таблица сопряженности (Churn и International plan)
crosstab_plan = pd.crosstab(data['International plan'], data['Churn'])
crosstab_plan_percentage = crosstab_plan.div(crosstab_plan.sum(axis=1), axis=0) * 100
print("\nТаблица сопряженности (International plan и Churn):")
print(crosstab_plan)
print("\nПроцент оттока среди клиентов с международным роумингом:")
print(crosstab_plan_percentage)

# Шаг 8: Добавление столбца "Прогнозируемый отток"
data['Predicted churn'] = (data['Customer service calls'] > high_churn_calls) | (data['International plan'] == 'Yes')

# Оценка ошибок первого и второго рода
false_positives = ((data['Predicted churn'] == True) & (data['Churn'] == False)).sum()
false_negatives = ((data['Predicted churn'] == False) & (data['Churn'] == True)).sum()

total_actual_churn = data['Churn'].sum()
total_actual_active = (~data['Churn']).sum()

error_type_1 = false_positives / total_actual_active * 100
error_type_2 = false_negatives / total_actual_churn * 100

print(f"\nОшибки первого рода (ложноположительные): {error_type_1:.2f}%")
print(f"Ошибки второго рода (ложноотрицательные): {error_type_2:.2f}%")
