# Write a Python program to count the number of lines in a text file.


# Открываем файл в режиме чтения
filename = "example.txt"  # Укажи свой файл
with open(filename, "r") as file:
    lines = file.readlines()  # Читаем все строки

# Подсчитываем количество строк
line_count = len(lines)

# Выводим результат
print(f"Number of lines in '{filename}': {line_count}")
