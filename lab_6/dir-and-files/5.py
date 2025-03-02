# Write a Python program to write a list to a file.

# Создаем список данных
data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Открываем файл в режиме записи
filename = "output.txt"
with open(filename, "w") as file:
    for item in data:
        file.write(item + "\n")