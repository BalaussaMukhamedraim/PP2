# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def numbers(n):
    for i in range(0, n + 1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

n = int(input("Enter a number: "))

print(",".join(map(str, numbers(n))))
