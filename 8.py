# Write a Python program to split a string at uppercase letters.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'(?=[A-Z])'
result = re.split(pattern, text_to_match)
print(result)