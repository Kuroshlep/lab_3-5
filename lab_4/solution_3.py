import pandas as pd

# 3.1. Загрузить датасет из файла marks.csv
data_marks = pd.read_csv("marks.csv", encoding='cp1251', delimiter=";")
print("Полное содержимое датасета:")
print(data_marks)

# 3.2. Вывести фамилии и оценки по математике для первых 50 учеников
print("\nФамилии и оценки по математике для первых 50 учеников:")
print(data_marks.loc[:49, ["Фамилия", "Математика"]])

# 3.3. Вывести фамилии учеников, имеющих оценку «5» по русскому языку
print("\nФамилии учеников с оценкой 5 по русскому языку:")
print(data_marks.loc[data_marks["Русский язык"] == 5, "Фамилия"])
