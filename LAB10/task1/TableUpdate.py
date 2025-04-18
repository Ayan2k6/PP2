import psycopg2
from config import host, user, password, db_name

def rename_contact(number, new_label):
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
                "UPDATE phonebook SET name = %s WHERE phonenumber = %s;",
                (new_label, number)
            )
            if cur.rowcount > 0:
                print("[INFO] Имя успешно изменено")
            else:
                print("[INFO] Пользователь с таким номером не найден")

    except psycopg2.Error as err:
        print("[ERROR] Ошибка при обновлении имени:", err)

    finally:
        if conn:
            conn.close()

def change_number(label, new_number):
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
                "UPDATE phonebook SET phonenumber = %s WHERE name = %s;",
                (new_number, label)
            )
            if cur.rowcount > 0:
                print("[INFO] Номер телефона успешно обновлён")
            else:
                print("[INFO] Контакт с таким именем не найден")

    except psycopg2.Error as err:
        print("[ERROR] Ошибка при обновлении номера:", err)

    finally:
        if conn:
            conn.close()

def main():
    action = input("Что вы хотите изменить? (name/phone): ").strip().lower()

    if action == "name":
        old_number = input("Введите текущий номер: ").strip()
        updated_name = input("Введите новое имя: ").strip()
        rename_contact(old_number, updated_name)
    elif action == "phone":
        existing_name = input("Введите имя контакта: ").strip()
        updated_number = input("Введите новый номер: ").strip()
        change_number(existing_name, updated_number)
    else:
        print("[WARN] Неизвестная команда. Введите 'name' или 'phone'.")

if __name__ == "__main__":
    main()