import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE cases
ADD COLUMN emergency_flag TEXT DEFAULT 'No'
""")

conn.commit()

conn.close()

print("Emergency Flag Column Added Successfully")