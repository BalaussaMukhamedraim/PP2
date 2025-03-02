# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
text = input("Enter a string: ")

upper = sum(map(str.isupper, text))
lower = sum(map(str.islower, text))

print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")