import psycopg2
from config import host, user, password, db_name

DELETE_QUERY = "DELETE FROM phonebook WHERE id = %s;"

def connect_to_db():
    return psycopg2.connect(
        host = host,
        user = user,
        password = password,
        dbname = db_name
    )

def remove_record():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        target = input("Что хотите удалить (phone/name)? ").strip().lower()
        record_id = input("Введите ID записи для удаления: ").strip()

        if target in ("phone", "name"):
            cur.execute(DELETE_QUERY, (record_id,))
            conn.commit()
            print("[INFO] Запись успешно удалена")
        else:
            print("[WARN] Неверный ввод. Введите 'phone' или 'name'")

    except psycopg2.Error as e:
        print(f"[ERROR] Ошибка при удалении: {e}")

    finally:
        if conn:
            cur.close()
            conn.close()
            print("[INFO] Соединение с базой данных закрыто")

if __name__ == "__main__":
    remove_record()