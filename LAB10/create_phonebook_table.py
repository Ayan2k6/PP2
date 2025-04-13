import psycopg2
from config import load_config

def create_phonebook_table():
    command = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print(" Table 'phonebook' created successfully.")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    create_phonebook_table()