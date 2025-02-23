import json
from tabulate import tabulate

# Открываем JSON-файл
with open("/Users/alia/Desktop/kbtu/PP2/lab_4/json/sample-data.json") as file:
    data = json.load(file)

# Список для хранения данных
table_data = []

# Проход по JSON и извлечение нужных данных
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    description = attributes.get("descr", "")  # Добавляем Description (может быть пустым)

    table_data.append([dn, description, speed, mtu])

# Заголовки
headers = ["DN", "Description", "Speed", "MTU"]

# Вывод заголовка Interface Status
print("Interface Status")

# Автоматически создаем разделители с tabulate
print(tabulate(table_data, headers=headers, tablefmt="double_outline"))
