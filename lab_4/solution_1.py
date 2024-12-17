import pandas as pd
import numpy as np

# 1.1. Сгенерировать случайный массив (Series) из 20 элементов
data = pd.Series(np.random.randint(1, 101, 20))
print("Случайный массив из 20 элементов:")
print(data)

# 1.2. Вывести элементы с номерами от 5 до 10 включительно
print("\nЭлементы с номерами от 5 до 10:")
print(data[5:11])

# 1.3. Вывести элементы со значениями от 10 до 50 включительно
print("\nЭлементы со значениями от 10 до 50:")
print(data[(data >= 10) & (data <= 50)])

# 1.4. Вывести только чётные элементы (с использованием лямбда-функции)
print("\nЧётные элементы:")
print(data[data.apply(lambda x: x % 2 == 0)])

# 1.5. Заменить все элементы, значение которых больше 70, на 0
data_modified = data.copy()
data_modified[data_modified > 70] = 0
print("\nМассив после замены элементов > 70 на 0:")
print(data_modified)
