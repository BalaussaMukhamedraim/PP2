# Implement a generator that returns all numbers from (n) down to 0.

def numbers(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number: "))

for i in numbers(n):
    print(i)