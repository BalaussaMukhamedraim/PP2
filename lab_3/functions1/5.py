def permutations(s, step=0):
    if step == len(s):
        print("".join(s))
    for i in range(step, len(s)):
        s = list(s)
        s[step], s[i] = s[i], s[step]
        permutations(s, step + 1)

def print_permutations():
    permutations(input("Enter a string: "))

print_permutations()
