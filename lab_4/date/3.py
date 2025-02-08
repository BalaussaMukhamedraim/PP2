# Write a Python program to drop microseconds from datetime.

import datetime

x = datetime.datetime.now()
y = x.replace(microsecond=0)

print("С микросекундами:", x)
print("Без микросекунд:", y)

