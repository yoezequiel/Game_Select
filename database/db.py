import sqlite3


def create_db():
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                grade INTEGER NOT NULL)"""
    )

    conn.commit()
    conn.close()
