import csv
import psycopg2
from config import user, db_name, password, host

def import_contacts(csv_path):
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname = db_name
        )
        conn.autocommit = True

        with conn.cursor() as cur, open(csv_path, newline = '', encoding = 'utf-8') as file:
            records = csv.DictReader(file)
            for contact in records:
                fullname = contact.get("name")
                phone = contact.get("phonenumber")
                cur.execute(
                    "INSERT INTO phonebook (name, phonenumber) VALUES (%s, %s);",
                    (fullname, phone)
                )
        print("[INFO] Контакты успешно импортированы")

    except psycopg2.Error as db_err:
        print("[ERROR] Ошибка при вставке данных:", db_err)

    except FileNotFoundError:
        print("[ERROR] CSV файл не найден")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    import_contacts("PP2/LAB10/task1/ContactsOfPeople.csv")