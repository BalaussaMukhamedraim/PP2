# Define a class which has at least two methods: getString: to get a string from console input 
# printString: to print the string in upper case.

class StringProcessor:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        self.user_string = input("Enter a string: ")

    def printString(self):
        print(self.user_string.upper())

p1 = StringProcessor()
p1.getString()
p1.printString()
