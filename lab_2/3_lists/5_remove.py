thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# the remove() method removes the first occurrence

print("-----")

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# If you do not specify the index, the pop() method removes the last item

print("-----")

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely.
# thislist = ["apple", "banana", "cherry"]
# del thislist
