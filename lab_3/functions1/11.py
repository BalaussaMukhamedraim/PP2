def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")  # Convert to lowercase & remove spaces and punctuation
    return s == s[::-1]  # Check if the string is equal to its reverse

# Example usage
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")