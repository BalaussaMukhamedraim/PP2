# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
with open("row.txt", "r") as file:
    text_to_match = file.read()

pattern = r'[\s,\.]'
result = re.sub(pattern, ":", text_to_match)
print(result)
# import re

# text_to_match = """
# John's email is john.doe@example.com
# Hello John
# """

# pattern = r'John'

# result = re.sub(pattern, "Johnny" ,text_to_match.strip()) 
# # splits the text by newlines

# print(result)