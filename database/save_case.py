import sqlite3

def save_case(data):

    conn = sqlite3.connect("hospital.db")

    cursor = conn.cursor()

    if data["urgency"] == "Emergency":

        emergency_flag = "Yes"

    else:

        emergency_flag = "No"

    cursor.execute(
        """
        INSERT INTO cases
        (
            patient_name,
            phone,
            symptoms,
            urgency,
            department,
            summary,
            status,
            emergency_flag
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["patient_name"],
            data["phone"],
            data["symptoms"],
            data["urgency"],
            data["department"],
            data["summary"],
            "Pending",
            emergency_flag
        )
    )

    conn.commit()
    conn.close()