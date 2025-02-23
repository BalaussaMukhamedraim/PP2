# Write a Python program to convert a given camel case string to snake case.

import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str

print(camel_to_snake('HelloGuysHowAreYou'))