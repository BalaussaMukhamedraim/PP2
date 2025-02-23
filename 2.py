# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = re.compile(r'ab{2,3}')

result = pattern.search(text_to_match)

if result:
    print(result.group(0))
else:
    print("Совпадений не найдено")