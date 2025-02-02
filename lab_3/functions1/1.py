# A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
class converter:
    def __init__(self, grams):
        self.grams = grams

    def __str__(self):
        ounces = 28.3495231 * self.grams
        return f"{ounces:.2f} ounces"

p1 = converter(5)
print(p1)