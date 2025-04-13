import psycopg2
import csv
from config import load_config

def insert_from_csv(file_path):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                            (row['name'].strip(), row['phone'].strip())
                        )
                print("Данные успешно добавлены из CSV!")
    except Exception as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    insert_from_csv("contacts.csv")