thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")