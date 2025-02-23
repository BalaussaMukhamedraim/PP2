# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'\b[a-z]+_[a-z]+\b'

result = re.findall(pattern, text_to_match)

print(result)