# Write a Python program to insert spaces between words starting with capital letters.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'(?<!\s)(?=[A-Z])'
result = re.split(pattern, text_to_match)
print(result)