import psycopg2
from config import host, user, password, db_name

QUERY_ALL = "SELECT * FROM phonebook;"
QUERY_BY_NAME = "SELECT * FROM phonebook WHERE name = %s;"
QUERY_BY_ID = "SELECT * FROM phonebook WHERE id = %s;"

def open_db():
    return psycopg2.connect(
        host = host,
        user = user,
        password = password,
        dbname = db_name
    )

def show_results():
    try:
        conn = open_db()
        cur = conn.cursor()

        option = input("Выберите тип запроса (all / name / id): ").strip().lower()

        if option == "all":
            cur.execute(QUERY_ALL)
            for row in cur.fetchall():
                print(row)
        elif option == "name":
            person = input("Введите имя: ")
            cur.execute(QUERY_BY_NAME, (person,))
            print(cur.fetchall())
        elif option == "id":
            record_id = input("Введите ID: ")
            cur.execute(QUERY_BY_ID, (record_id,))
            print(cur.fetchone())
        else:
            print("[WARN] Неизвестная команда запроса")

    except psycopg2.Error as e:
        print(f"[ERROR] Ошибка при выполнении запроса: {e}")
    
    finally:
        if conn:
            cur.close()
            conn.close()
            print("[INFO] Соединение закрыто")

if __name__ == "__main__":
    show_results()