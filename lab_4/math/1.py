# Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904

# Write a Python program to convert degree to radian.

import math

# Ввод угла в градусах
degree = float(input("Введите угол в градусах: "))

# Конвертация градусов в радианы
radian = math.radians(degree)  # Используем встроенную функцию

# Вывод результата с округлением до 6 знаков
print("Радианы:", round(radian, 6))

