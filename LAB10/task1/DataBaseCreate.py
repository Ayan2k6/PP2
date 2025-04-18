import psycopg2
import csv
from config import host, user, password, db_name

def open_connection():
    return psycopg2.connect(
        host = host,
        user = user,
        password = password,
        dbname = db_name
    )

def create_phonebook_table():
    conn=None
    try:
        conn = open_connection()
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print(f"[INFO] Connected to: {cur.fetchone()}")

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    PhoneNumber VARCHAR(15) NOT NULL
                );
            """)
            print("[INFO] Phonebook table created")

    except psycopg2.Error as err:
        print(f"[ERROR] PostgreSQL issue: {err}")
    
    finally:
        if conn:
            conn.close()
            print("[INFO] Connection to PostgreSQL closed")

if __name__ == "__main__":
    create_phonebook_table()