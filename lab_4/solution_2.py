import pandas as pd
import numpy as np

# 2.1. Создать объект Series с пустыми значениями
data_with_nan = pd.Series([1, 2, np.nan, 3, 4, np.nan, 7, 8, np.nan, 10])
print("Объект Series с пустыми значениями:")
print(data_with_nan)

# 2.2. Вывести только непустые значения
print("\nТолько непустые значения:")
print(data_with_nan.dropna())

# 2.3. Извлечь квадратный корень из каждого элемента
print("\nКвадратный корень из каждого элемента:")
print(data_with_nan.apply(lambda x: np.sqrt(x) if not pd.isna(x) else np.nan))

# 2.4. Заменить все пустые значения на -1
data_filled = data_with_nan.fillna(-1)
print("\nОбъект Series после замены NaN на -1:")
print(data_filled)
