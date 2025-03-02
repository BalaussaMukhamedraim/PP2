# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

text = input("Enter a string: ")
is_palindrome = text.lower() == text[::-1].lower()

print("Palindrome" if is_palindrome else "Not a palindrome")