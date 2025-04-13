import psycopg2
from config import load_config

def delete_contact():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                print(" Удаление записи из PhoneBook")
                option = input("Удалить по имени (1) или по номеру (2)? Введите 1 или 2: ").strip()

                if option == '1':
                    name = input("Введите имя для удаления: ").strip()
                    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
                elif option == '2':
                    phone = input("Введите номер для удаления: ").strip()
                    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                else:
                    print(" Неверный вариант.")
                    return

                if cur.rowcount == 0:
                    print("⚠️ Ни одна запись не была удалена.")
                else:
                    print(f" Удалено записей: {cur.rowcount}")

    except Exception as e:
        print("Ошибка при удалении:", e)

if __name__ == '__main__':
    delete_contact()