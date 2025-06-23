import sqlite3

DB_NAME = "students.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            grade REAL NOT NULL
        )
        """)
        conn.commit()


def get_all_students():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute(
            "SELECT id, first_name, last_name, email, grade FROM students"
        ).fetchall()


def get_student(student_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute(
            "SELECT id, first_name, last_name, email, grade FROM students WHERE id=?", (student_id,)
        ).fetchone()


def insert_student(first_name, last_name, email, grade):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, grade) VALUES (?, ?, ?, ?)",
            (first_name, last_name, email, grade),
        )
        conn.commit()
        return cur.lastrowid


def update_student(student_id, first_name, last_name, email, grade):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "UPDATE students SET first_name=?, last_name=?, email=?, grade=? WHERE id=?",
            (first_name, last_name, email, grade, student_id),
        )
        conn.commit()


def delete_student(student_id):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "DELETE FROM students WHERE id=?", (student_id,)
        )
        conn.commit()
