# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

path = './' # relative path
# .. - shorthand for previous directory
# .  - shorthand for current directory

contents = os.listdir(path)
# Разделяем на файлы и папки
directories = [d for d in contents if os.path.isdir(os.path.join(path, d))]
files = [f for f in contents if os.path.isfile(os.path.join(path, f))]

# Выводим отдельно
print("Directories:")
for d in directories:
    print(d)

print("\nFiles:")
for f in files:
    print(f)

print("\nAll contents:")
for element in contents:
    print(element)
    