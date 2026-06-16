import sqlite3

def save_appointment(
    case_id,
    appointment_date,
    appointment_time
):

    conn = sqlite3.connect("hospital.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO appointments
        (
            case_id,
            appointment_date,
            appointment_time,
            status
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            case_id,
            appointment_date,
            appointment_time,
            "Booked"
        )
    )

    conn.commit()
    conn.close()