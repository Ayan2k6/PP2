import psycopg2
from ConfigSnakeGame import host, user, password, db_name

def initialize_database():
    conn = None
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname = db_name
        )

        cur = conn.cursor()
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            score INT DEFAULT 0,
            level INT DEFAULT 1
        );
        """
        cur.execute(create_users_table)
        conn.commit()
        print("[INFO] User table initialized")

    except psycopg2.Error as error:
        print(f"[ERROR] Failed to initialize DB: {error}")

    finally:
        if conn:
            conn.close()
            print("[INFO] Connection closed")

if __name__ == "__main__":
    initialize_database()