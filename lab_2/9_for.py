# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("-------")

for x in "banana":
  print(x)

print("-------")

# break 
# With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

print("-------")
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("-------")
# continue 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("-------")

# The range() Function
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6):
  print(x)

print("-------")

# range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)

print("-------")

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

print("-------")

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# The else block will NOT be executed if the loop is stopped by a break statement.
print("-------")
# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print("-------")

# Nested Loops
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass