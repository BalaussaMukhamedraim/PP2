# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z)



# What if no items are present in both sets?
# Return False if one or more items are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y) 
print(z)