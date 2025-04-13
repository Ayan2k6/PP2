import psycopg2
from config import load_config

def update_contact():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                print(" Обновление записи в PhoneBook")
                option = input("Обновить по имени (1) или по номеру (2)? Введите 1 или 2: ").strip()

                if option == '1':
                    old_name = input("Введите имя, которое нужно обновить: ").strip()
                    new_phone = input("Введите новый номер: ").strip()
                    cur.execute(
                        "UPDATE phonebook SET phone = %s WHERE name = %s",
                        (new_phone, old_name)
                    )

                elif option == '2':
                    old_phone = input("Введите номер, который нужно обновить: ").strip()
                    new_name = input("Введите новое имя: ").strip()
                    cur.execute(
                        "UPDATE phonebook SET name = %s WHERE phone = %s",
                        (new_name, old_phone)
                    )
                else:
                    print(" Неверный вариант.")
                    return

                if cur.rowcount == 0:
                    print("⚠️ Ни одна запись не была обновлена.")
                    print(f"DEBUG: Введённый номер → {old_phone if option == '2' else old_name}")
                else:
                    print(" Запись успешно обновлена!")

    except Exception as e:
        print(" Ошибка при обновлении:", e)

if __name__ == '__main__':
    update_contact()