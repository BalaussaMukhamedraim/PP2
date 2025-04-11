import psycopg2
import csv

conn = psycopg2.connect(
    dbname = "lab10",
    user = "postgres",
    password = "12345678",
    host="localhost",
    port="5432" 
)

print("Успешное подключение к базе данных!")

cur = conn.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id serial PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
            );
""")
conn.commit()

def upload_from_csv():
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", row)
    conn.commit()
    print("Данные загружены из CSV.")

def add_manually():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone) )
    conn.commit()
    print("Контакт добавлен.")

def update_contact():
    name = input("Введите имя контакта, который хотите обновить: ")
    choice = input("Что обновить? (1 - имя, 2 - телефон): ")
    if choice == "1":
        new_name = input("Введите новое имя: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE firstname = %s", (new_name, name))
    elif choice == "2":
        new_phone = input("Введите новый номер телефона: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()
    print("Контакт обновлен.")

def search_contact():
    filter_by = input("Фильтровать по (1 - имя, 2 - телефон): ")
    if filter_by == "1":
        name = input("Имя: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    elif filter_by == "2":
        phone = input("Телефон: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_contact():
    by = input("Удалить по (1 - имя, 2 - телефон): ")
    if by == "1":
        name = input("Имя: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif by == "2":
        phone = input("Телефон: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Контакт удалён.")

# Меню
while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Загрузить из CSV")
    print("2. Добавить вручную")
    print("3. Обновить контакт")
    print("4. Найти контакт")
    print("5. Удалить контакт")
    print("0. Выйти")

    option = input("Выберите опцию: ")

    if option == "1":
        upload_from_csv()
    elif option == "2":
        add_manually()
    elif option == "3":
        update_contact()
    elif option == "4":
        search_contact()
    elif option == "5":
        delete_contact()
    elif option == "0":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")

# Закрытие соединения
cur.close()
conn.close()
