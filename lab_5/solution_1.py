import numpy as np
import pandas as pd

# Шаг 1: Создание массива нормально распределенных случайных величин
M = 1.0  # математическое ожидание
S = 1.0  # стандартное отклонение
size = 1000  # количество элементов

data = np.random.normal(loc=M, scale=S, size=size)
series = pd.Series(data)

# Шаг 2: Доля значений в диапазоне (M-S; M+S)
in_one_sigma = ((series > (M - S)) & (series < (M + S))).mean()
print(f"Доля значений в диапазоне (M-S; M+S): {in_one_sigma:.2%}")

# Шаг 3: Доля значений в диапазоне (M-3S; M+3S)
in_three_sigma = ((series > (M - 3*S)) & (series < (M + 3*S))).mean()
print(f"Доля значений в диапазоне (M-3S; M+3S): {in_three_sigma:.2%}")

# Теоретическая доля для трех сигм
theoretical_three_sigma = 0.9973
print(f"Теоретическая доля в пределах трех сигм: {theoretical_three_sigma:.2%}")

# Шаг 4: Преобразование значений в их квадратные корни
sqrt_series = series.apply(lambda x: np.sqrt(x) if x >= 0 else np.nan)
print(f"Количество NaN после преобразования: {sqrt_series.isna().sum()}")

# Шаг 5: Среднее арифметическое
mean_sqrt = sqrt_series.mean()
print(f"Среднее арифметическое значений после преобразования: {mean_sqrt:.2f}")

# Шаг 6: Создание DataFrame
df = pd.DataFrame({'number': series, 'root': sqrt_series})
print("Первые 6 строк DataFrame:")
print(df.head(6))

# Шаг 7: Фильтрация значений квадратного корня в диапазоне от 1.8 до 1.9
filtered = df.query("1.8 <= root <= 1.9")
print("Результаты фильтрации:")
print(filtered)
