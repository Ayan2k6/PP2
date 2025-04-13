import psycopg2
from config import load_config

def insert_contact(name, phone):
    query = """
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (name, phone))
                print(f"✅ Contact '{name}' added successfully.")
    except Exception as e:
        print(" Error inserting contact:", e)

if __name__ == '__main__':
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    insert_contact(name, phone)