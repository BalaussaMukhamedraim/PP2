# Write a python program to convert snake case string to camel case string.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'_([a-z])'
result = re.sub(pattern, lambda m: m.group(1).upper(), text_to_match)
print(result)