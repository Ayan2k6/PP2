import psycopg2
import csv
from tabulate import tabulate
from config import host, user, password, db_name

def open_connection():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name
    )

def insert_data():
    conn = open_connection()
    cur = conn.cursor()
    method = input('Type "csv" or "con" (upload CSV / console insert): ').strip().lower()
    if method == "con":
        name    = input("Name: ").strip()
        surname = input("Surname: ").strip()
        phone   = input("Phone: ").strip()
        cur.execute(
            "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s);",
            (name, surname, phone)
        )
        print("[INFO] Contact added")
    elif method == "csv":
        path = input("Enter CSV file path: ").strip()
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # пропускаем заголовок
                for row in reader:
                    cur.execute(
                        "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s);",
                        (row[0], row[1], row[2])
                    )
            print("[INFO] Contacts imported from CSV")
        except FileNotFoundError:
            print("[ERROR] CSV file not found")
    else:
        print("[WARN] Unknown insert method")
    conn.commit()
    cur.close()
    conn.close()

def update_data():
    conn = open_connection()
    cur = conn.cursor()
    # На выбор: менять имя или телефон
    choice = input('What to update? Type "name" or "phone": ').strip().lower()
    if choice == "name":
        old_phone = input("Enter current phone to identify contact: ").strip()
        new_name  = input("Enter new name: ").strip()
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE phone = %s;",
            (new_name, old_phone)
        )
    elif choice == "phone":
        name      = input("Enter contact name to identify record: ").strip()
        new_phone = input("Enter new phone: ").strip()
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s;",
            (new_phone, name)
        )
    else:
        print("[WARN] Unknown update choice")
        conn.close()
        return

    conn.commit()
    print(f"[INFO] {cur.rowcount} row(s) updated")
    cur.close()
    conn.close()

def delete_data():
    conn = open_connection()
    cur = conn.cursor()
    phone = input("Enter phone number to delete: ").strip()
    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s;",
        (phone,)
    )
    conn.commit()
    print(f"[INFO] {cur.rowcount} row(s) deleted")
    cur.close()
    conn.close()

def query_data():
    conn = open_connection()
    cur = conn.cursor()
    column = input("Search by which column? (name/surname/phone): ").strip().lower()
    if column not in ("name", "surname", "phone"):
        print("[WARN] Invalid column")
        conn.close()
        return
    value = input(f"Enter {column}: ").strip()
    sql = f"SELECT * FROM phonebook WHERE {column} = %s;"
    cur.execute(sql, (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID","Name","Surname","Phone"], tablefmt="fancy_grid"))
    cur.close()
    conn.close()

def display_data():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID","Name","Surname","Phone"], tablefmt="fancy_grid"))
    cur.close()
    conn.close()

if __name__ == "__main__":
    while True:
        print("""
        Commands:
         i - INSERT (console or CSV)
         u - UPDATE (name or phone)
         q - QUERY specific record
         d - DELETE by phone
         s - SHOW all
         f - FINISH / exit
        """)
        cmd = input("Enter command: ").strip().lower()
        if   cmd == "i": insert_data()
        elif cmd == "u": update_data()
        elif cmd == "q": query_data()
        elif cmd == "d": delete_data()
        elif cmd == "s": display_data()
        elif cmd == "f": 
            print("Goodbye!")
            break
        else:
            print("[WARN] Unknown command")
