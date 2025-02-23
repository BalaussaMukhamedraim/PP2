# Sets are used to store multiple items in a single variable.
# Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets cannot have two items with the same value.

# The values True and 1 are considered the same value in sets, and are treated as duplicates
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)


# False and 0 is considered the same value:
# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}



# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)