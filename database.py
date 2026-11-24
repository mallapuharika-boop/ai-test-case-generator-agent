
import sqlite3
import json

DB_NAME = "test_cases.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requirement TEXT NOT NULL,
            results TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def save_history(requirement, results):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (requirement, results) VALUES (?, ?)",
        (requirement, json.dumps(results))
    )

    conn.commit()
    conn.close()

def get_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, requirement, results, created_at FROM history ORDER BY id DESC"
    )

    records = cursor.fetchall()
    conn.close()
    return records
