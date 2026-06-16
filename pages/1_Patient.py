import streamlit as st
import sqlite3
from graph.workflow import graph
from database.save_case import save_case

st.set_page_config(
    page_title="Patient Dashboard",
    layout="wide"
)

st.title("👤 Patient Dashboard")
st.subheader("📝 Register New Case")

patient_name = st.text_input(
    "Patient Name"
)

phone_input = st.text_input(
    "Phone Number"
)

symptoms_input = st.text_area(
    "Describe Your Symptoms"
)

if st.button("Submit Case"):

    if patient_name and phone_input and symptoms_input:

        result = graph.invoke({
            "patient_name": patient_name,
            "phone": phone_input,
            "symptoms": symptoms_input
        })

        save_case(result)

        st.success(
            "Case Submitted Successfully!"
        )

    else:

        st.warning(
            "Please fill all fields."
        )

st.divider()

if "phone" not in st.session_state:
    st.session_state.phone = ""

phone = st.text_input(
    "Enter Phone Number",
    value=st.session_state.phone
)

if st.button("View My Cases"):
    st.session_state.phone = phone

if st.session_state.phone:

    conn = sqlite3.connect("hospital.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            patient_name,
            symptoms,
            urgency,
            department,
            summary
        FROM cases
        WHERE phone=?
        ORDER BY id DESC
        """,
        (st.session_state.phone,)
    )

    cases = cursor.fetchall()

    if not cases:

        st.error(
            "No cases found."
        )

    else:

        for case in cases:

            (
                case_id,
                patient_name,
                symptoms,
                urgency,
                department,
                summary
            ) = case

            with st.expander(
                f"Case #{case_id}"
            ):

                st.subheader("Patient Details")

                st.write(
                    "Patient:",
                    patient_name
                )

                st.write(
                    "Symptoms:",
                    symptoms
                )

                st.write(
                    "Urgency:",
                    urgency
                )

                st.write(
                    "Department:",
                    department
                )

                st.subheader(
                    "AI Summary"
                )

                st.write(summary)

                # Doctor Responses
                cursor.execute(
                    """
                    SELECT response
                    FROM doctor_responses
                    WHERE case_id=?
                    ORDER BY id DESC
                    """,
                    (case_id,)
                )

                responses = cursor.fetchall()

                st.subheader(
                    "Doctor Responses"
                )

                if responses:

                    for response in responses:

                        st.success(
                            response[0]
                        )

                else:

                    st.warning(
                        "No doctor response yet."
                    )

                st.divider()

                # Appointment Booking
                st.subheader(
                    "Book Appointment"
                )

                appointment_date = st.date_input(
                    "Select Date",
                    key=f"date_{case_id}"
                )

                all_slots = [
                    "10:00 AM",
                    "11:30 AM",
                    "02:00 PM",
                    "04:00 PM"
                ]

                cursor.execute(
                    """
                    SELECT appointment_time
                    FROM appointments
                    WHERE appointment_date=?
                    """,
                    (str(appointment_date),)
                )

                booked_slots = [
                    row[0]
                    for row in cursor.fetchall()
                ]

                available_slots = [
                    slot
                    for slot in all_slots
                    if slot not in booked_slots
                ]

                if available_slots:

                    appointment_time = st.selectbox(
                        "Available Slots",
                        available_slots,
                        key=f"slot_{case_id}"
                    )

                    if st.button(
                        "Book Appointment",
                        key=f"book_{case_id}"
                    ):

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
                                str(appointment_date),
                                appointment_time,
                                "Booked"
                            )
                        )

                        conn.commit()

                        st.success(
                            "Appointment Booked Successfully"
                        )
                        st.rerun()

                else:

                    st.error(
                        "No available slots for this date."
                    )

                st.divider()

                # Current Appointment
                st.subheader(
                    "Current Appointment"
                )

                cursor.execute(
                    """
                    SELECT
                        appointment_date,
                        appointment_time,
                        status
                    FROM appointments
                    WHERE case_id=?
                    ORDER BY id DESC
                    LIMIT 1
                    """,
                    (case_id,)
                )

                appointment = cursor.fetchone()

                if appointment:

                    date, time, status = appointment

                    st.info(
                        f"""
Date: {date}

Time: {time}

Status: {status}
"""
                    )

                else:

                    st.warning(
                        "No appointment booked yet."
                    )

    conn.close()