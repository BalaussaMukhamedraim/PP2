thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# sort() method is case sensitive; matters lower and upper cases

print("------")

# case insensitive example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


print("------")

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

