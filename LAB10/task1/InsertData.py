import psycopg2
from config import host, user, password, db_name

def add_contact(person, number):
    conn = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname = db_name
        )
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook (name, phonenumber) VALUES (%s, %s);",
                (person, number)
            )
            print("[INFO] Контакт добавлен")

    except psycopg2.Error as err:
        print(f"[ERROR] При добавлении произошла ошибка: {err}")

    finally:
        if conn:
            conn.close()
            print("[INFO] Соединение закрыто")

if __name__ == "__main__":
    contact_name = input("Введите имя: ")
    contact_number = input("Введите номер: ")
    add_contact(contact_name, contact_number)