# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

# Ввод пути для проверки
path = input("Enter a path: ")

# Проверяем доступ
print(f"Path exists: {os.path.exists(path)}")
print(f"Readable: {os.access(path, os.R_OK)}")
print(f"Writable: {os.access(path, os.W_OK)}")
print(f"Executable: {os.access(path, os.X_OK)}")

