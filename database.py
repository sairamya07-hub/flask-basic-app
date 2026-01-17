import sqlite3

def get_connection():
    conn = sqlite3.connect("app.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
def insert_user(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        (name,)
    )

    conn.commit()
    conn.close()
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM users")
    users = cursor.fetchall()

    conn.close()
    return users
