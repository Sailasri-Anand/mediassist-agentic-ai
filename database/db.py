import sqlite3

def init_db():

    conn = sqlite3.connect("hospital.db")

    cursor = conn.cursor()

    # Cases Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cases(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        phone TEXT,
        symptoms TEXT,
        urgency TEXT,
        department TEXT,
        summary TEXT,
        status TEXT DEFAULT 'Pending'
        emergency_flag TEXT DEFAULT 'No'
    )
    """)

    # Doctor Responses Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctor_responses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        response TEXT
    )
    """)

    # Appointments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        appointment_date TEXT,
        appointment_time TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()