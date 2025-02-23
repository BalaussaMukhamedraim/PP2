# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# import re
# # txt_file = '../row.txt'
# with open("row.txt", "r") as file:
#     text_to_match = file.read()

# # pattern = re.findall('ab+')

# result = re.findall('ab+', text_to_match)

# print(result)

import re

with open("row.txt", "r") as file:
    text_to_match = file.read()


pattern = re.compile(r'ab+')
# Используем search(), чтобы найти первое совпадение
result = pattern.search(text_to_match)

if result:
    print(result.group(0))
else:
    print("Совпадений не найдено")
