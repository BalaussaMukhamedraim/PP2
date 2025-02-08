# Write a Python program to subtract five days from current date.

import datetime

current_date = datetime.datetime.now()

five_days_ago = current_date - datetime.timedelta(days=5)

print("Сегодня:", current_date.strftime("%Y-%m-%d"))
print("5 дней назад:", five_days_ago.strftime("%Y-%m-%d"))

