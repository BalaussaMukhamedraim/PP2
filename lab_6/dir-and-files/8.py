# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

# Ввод пути к файлу
file_path = input("Enter the file path to delete: ")

# Проверяем, существует ли файл
if os.path.exists(file_path):
    # Проверяем доступ на запись (нужно для удаления)
    if os.access(file_path, os.W_OK):
        os.remove(file_path)  # Удаляем файл
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"No write access to delete '{file_path}'.")
else:
    print("File does not exist.")