# Write a Python program to copy the contents of a file to another file

# Открываем исходный и целевой файлы
source_file = "source.txt"   # Исходный файл
destination_file = "copy.txt"  # Файл-копия

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    dest.write(src.read())  # Читаем и записываем весь контент

print(f"Contents of '{source_file}' copied to '{destination_file}'.")