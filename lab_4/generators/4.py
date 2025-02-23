# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def sqaures(a, b):
    for i in range(a, b + 1):
        i = i * i
        yield i

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

for i in sqaures(a, b):
    print(i)