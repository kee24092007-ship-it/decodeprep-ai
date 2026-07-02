import sqlite3

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def create_connection():
    return sqlite3.connect(
        "users.db",
        check_same_thread=False
    )

# -----------------------------
# CREATE TABLE
# -----------------------------
def create_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password BLOB NOT NULL

    )
    """)

    conn.commit()
    conn.close()

# -----------------------------
# RUN FILE
# -----------------------------
if __name__ == "__main__":
    create_table()
    print("✅ Users table created successfully!")