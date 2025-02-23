# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'a.*?b'
result = re.findall(pattern, text_to_match)

print(result)