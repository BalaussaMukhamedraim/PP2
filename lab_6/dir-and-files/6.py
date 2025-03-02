# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import os
import string

# Директория, куда будем сохранять файлы (по желанию)
output_dir = "alphabet_files"

# Создаем папку, если её нет
os.makedirs(output_dir, exist_ok=True)

# Генерируем 26 файлов (от A.txt до Z.txt)
for letter in string.ascii_uppercase:  # Генерирует 'A' - 'Z'
    filename = os.path.join(output_dir, f"{letter}.txt")
    with open(filename, "w") as file:
        file.write(f"This is file {letter}.txt\n")  # Записываем в файл
    print(f"Created: {filename}")

print("All 26 files have been created.")