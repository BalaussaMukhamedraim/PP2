# Write a Python program to calculate two date difference in seconds.
# import math
import datetime

current_date = datetime.datetime.now()
fixed_date = datetime.datetime(2022, 2, 1, 12, 0, 0)

difference = round(abs((current_date - fixed_date).total_seconds()), 2)

print("Текущая дата", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Фиксированная дата", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Разница в секундах", difference)

