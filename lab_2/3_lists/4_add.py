# append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("-----")

# insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print("-----")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("-----")

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)