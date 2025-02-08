# Write a Python program to print yesterday, today, tomorrow.

import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Вчера: ", yesterday.strftime("%Y-%m-%d"))
print("Сегодня: ", today.strftime("%Y-%m-%d"))
print("Завтра: ", tomorrow.strftime("%Y-%m-%d"))