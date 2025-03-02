# Write a Python program with builtin function that returns True if all elements of the tuple are true.

# Создаем кортеж
t = (True, 1, "Hello", [1, 2], 3.14)

# Проверяем, все ли элементы истинны
result = all(t)

# Вывод результата
print(result)

# код с for
# # Создаем кортеж
# t = (True, 1, "Hello", [1, 2], 3.14)

# Проверяем, все ли элементы истинны
# result = True  # Изначально предполагаем, что все элементы True

# for item in t:
#     if not item:  # Если хотя бы один элемент False
#         result = False
#         break  # Дальше проверять не нужно, можно сразу выйти

# Вывод результата
# print(result)