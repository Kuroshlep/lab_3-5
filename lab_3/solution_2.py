import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# 1. Загрузка данных из файла
data = np.genfromtxt('data2.csv', delimiter=';', skip_header=1)
discounts = data[:, 0]  # Скидки
profits = data[:, 1]    # Прибыль

# 2. Функция для решения СЛУ и построения полинома
def fit_polynomial(x, y, degree):
    """
    Построение полинома заданной степени.
    Возвращает коэффициенты и значения полинома.
    """
    n_points = degree + 1
    selected_indices = np.linspace(0, len(x) - 1, n_points, dtype=int)
    x_selected = x[selected_indices]
    y_selected = y[selected_indices]

    # Формируем матрицу СЛУ для полинома
    A = np.vander(x_selected, N=n_points, increasing=True)
    b = y_selected

    # Решаем СЛУ
    coeffs = solve(A, b)

    # Вычисляем значения полинома
    poly_values = np.polyval(coeffs[::-1], x)
    return coeffs, poly_values

# 3. Полином второй степени
coeffs_quad, poly_quad = fit_polynomial(discounts, profits, degree=2)

# 4. Полином третьей степени
coeffs_cubic, poly_cubic = fit_polynomial(discounts, profits, degree=3)

# 5. Вычисление RSS
def calculate_rss(y_true, y_pred):
    return np.sum((y_true - y_pred) ** 2)

rss_quad = calculate_rss(profits, poly_quad)
rss_cubic = calculate_rss(profits, poly_cubic)

# 6. Построение графиков
plt.figure(figsize=(10, 6))
plt.scatter(discounts, profits, color='blue', label='Исходные данные')
plt.plot(discounts, poly_quad, color='red', label=f'Полином 2-й степени (RSS={rss_quad:.2f})')
plt.plot(discounts, poly_cubic, color='green', label=f'Полином 3-й степени (RSS={rss_cubic:.2f})')
plt.xlabel('Скидка (%)')
plt.ylabel('Прибыль')
plt.title('Зависимость прибыли от скидки')
plt.legend()
plt.grid()
plt.show()

# 7. Выбор лучшего полинома и расчёт значений для скидок 6% и 8%
if rss_quad < rss_cubic:
    print("Полином 2-й степени выбран как лучший.")
    best_coeffs = coeffs_quad
else:
    print("Полином 3-й степени выбран как лучший.")
    best_coeffs = coeffs_cubic

# Расчёт прибыли при скидках 6% и 8%
profit_6 = np.polyval(best_coeffs[::-1], 6)
profit_8 = np.polyval(best_coeffs[::-1], 8)

print(f"Ожидаемая прибыль при скидке 6%: {profit_6:.2f}")
print(f"Ожидаемая прибыль при скидке 8%: {profit_8:.2f}")