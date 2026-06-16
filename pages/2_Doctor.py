import streamlit as st
import sqlite3

st.title("🏥 MediAssist Doctor Dashboard")

conn = sqlite3.connect(
    "hospital.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    id,
    patient_name,
    phone,
    symptoms,
    urgency,
    department,
    summary,
    status,
    emergency_flag
FROM cases
               
ORDER BY id DESC
""")

cases = cursor.fetchall()

if not cases:

    st.warning("No patient cases found.")

else:

    for case in cases:

        (
            case_id,
            patient_name,
            phone,
            symptoms,
            urgency,
            department,
            summary,
            status,
            emergency_flag
        ) = case

        with st.expander(
            f"Case #{case_id} | {patient_name} | {department}"
        ):
            if emergency_flag == "Yes":

                  st.error(
                     "🚨 HIGH PRIORITY EMERGENCY CASE"
                    )

            # Patient Details
            st.subheader("👤 Patient Details")

            st.write("Name:", patient_name)
            st.write("Phone:", phone)

            # Symptoms
            st.subheader("🩺 Symptoms")
            st.write(symptoms)

            # Urgency
            st.subheader("🚨 Urgency")

            if urgency == "Emergency":

                st.error(
                    f"🚨 {urgency}"
                )

            else:

                st.success(
                    urgency
                )

            # AI Summary
            st.subheader("🤖 AI Summary")
            st.write(summary)

            # Case Status
            st.subheader("📌 Case Status")

            if status == "Completed":

                st.success(
                    "✅ Completed"
                )

            else:

                st.warning(
                    "⏳ Pending"
                )

            st.divider()

            # Mark Completed Button
            if status != "Completed":

                if st.button(
                    "✅ Mark Completed",
                    key=f"complete_{case_id}"
                ):

                    cursor.execute(
                        """
                        UPDATE cases
                        SET status='Completed'
                        WHERE id=?
                        """,
                        (case_id,)
                    )

                    conn.commit()

                    st.success(
                        "Case Marked Completed"
                    )

                    st.rerun()

            st.divider()

            # Doctor Responses
            st.subheader(
                "💬 Doctor Responses"
            )

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

            if responses:

                for response in responses:

                    st.success(
                        response[0]
                    )

            else:

                st.info(
                    "No responses yet."
                )

            st.divider()

            # Appointment Status
            st.subheader(
                "📅 Appointment Status"
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

                (
                    appointment_date,
                    appointment_time,
                    appointment_status
                ) = appointment

                st.success(
                    f"""
Appointment Date: {appointment_date}

Appointment Time: {appointment_time}

Status: {appointment_status}
"""
                )

            else:

                st.warning(
                    "⏳ Patient has not booked an appointment yet."
                )

            st.divider()

            # New Doctor Response
            st.subheader(
                "✍️ Send New Response"
            )

            doctor_response = st.text_area(
                "Doctor Response",
                key=f"response_{case_id}"
            )

            if st.button(
                "Send Response",
                key=f"send_{case_id}"
            ):

                if doctor_response.strip():

                    cursor.execute(
                        """
                        INSERT INTO doctor_responses
                        (
                            case_id,
                            response
                        )
                        VALUES (?, ?)
                        """,
                        (
                            case_id,
                            doctor_response
                        )
                    )

                    conn.commit()

                    st.success(
                        "✅ Response Saved Successfully"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Please enter a response."
                    )

conn.close()