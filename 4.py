# Write a Python program to find the sequences of one upper case letter followed by lower case letters.


import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'\b[A-Z][a-z]+\b'

result = re.findall(pattern, text_to_match)

print(result)