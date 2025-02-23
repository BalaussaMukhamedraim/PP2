# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

class Convert:
    def __init__(self, gradus):
        self.gradus = gradus

    def __str__(self):
        centigrade = (5 / 9) * (self.gradus - 32)
        return f"{centigrade:.2f} centigrade"

p1 = Convert(48)
print(p1)

    


