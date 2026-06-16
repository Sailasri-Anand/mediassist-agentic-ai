import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="MediAssist Admin Dashboard",
    layout="wide"
)

st.title("🏥 MediAssist Admin Dashboard")

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# ==========================
# Dashboard Metrics
# ==========================

cursor.execute(
    "SELECT COUNT(*) FROM cases"
)
total_cases = cursor.fetchone()[0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM cases
    WHERE urgency='Emergency'
    """
)
emergency_cases = cursor.fetchone()[0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM appointments
    """
)
total_appointments = cursor.fetchone()[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Cases",
        total_cases
    )

with col2:
    st.metric(
        "Emergency Cases",
        emergency_cases
    )

with col3:
    st.metric(
        "Appointments",
        total_appointments
    )

st.divider()

st.subheader(
    "🚨 Active Emergency Cases"
)

cursor.execute(
    """
    SELECT
        patient_name,
        phone,
        department
    FROM cases
    WHERE emergency_flag='Yes'
    AND status!='Completed'
    """
)

emergency_cases = cursor.fetchall()

if emergency_cases:

    for patient in emergency_cases:

        st.error(
            f"""
Patient: {patient[0]}

Phone: {patient[1]}

Department: {patient[2]}
"""
        )

else:

    st.success(
        "No Active Emergency Cases"
    )

# ==========================
# Emergency Cases
# ==========================

st.subheader("🚨 Emergency Cases")

cursor.execute(
    """
    SELECT
        id,
        patient_name,
        phone,
        symptoms,
        department
    FROM cases
    WHERE urgency='Emergency'
    ORDER BY id DESC
    """
)

rows = cursor.fetchall()

if rows:

    df = pd.DataFrame(
        rows,
        columns=[
            "Case ID",
            "Patient",
            "Phone",
            "Symptoms",
            "Department"
        ]
    )

    df.insert(
        0,
        "S.No",
        range(1, len(df) + 1)
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.success(
        "No Emergency Cases"
    )

st.divider()

# ==========================
# All Patients
# ==========================

st.subheader("👥 All Patient Cases")

cursor.execute(
    """
    SELECT
        id,
        patient_name,
        phone,
        symptoms,
        urgency,
        department
    FROM cases
    ORDER BY id DESC
    """
)

all_cases = cursor.fetchall()

if all_cases:

    all_df = pd.DataFrame(
        all_cases,
        columns=[
            "Case ID",
            "Patient",
            "Phone",
            "Symptoms",
            "Urgency",
            "Department"
        ]
    )

    

    st.dataframe(
        all_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("🗑️ Delete Patient Case")

case_id_to_delete = st.number_input(
    "Enter Case ID to Delete",
    min_value=1,
    step=1
)

if st.button("Delete Case"):

    cursor.execute(
        """
        DELETE FROM doctor_responses
        WHERE case_id=?
        """,
        (case_id_to_delete,)
    )

    cursor.execute(
        """
        DELETE FROM appointments
        WHERE case_id=?
        """,
        (case_id_to_delete,)
    )

    cursor.execute(
        """
        DELETE FROM cases
        WHERE id=?
        """,
        (case_id_to_delete,)
    )

    conn.commit()

    st.success(
        f"Case #{case_id_to_delete} deleted successfully."
    )

    st.rerun()

st.divider()

# ==========================
# Department Analytics
# ==========================

st.subheader("📊 Department Distribution")

cursor.execute(
    """
    SELECT
        department,
        COUNT(*)
    FROM cases
    GROUP BY department
    """
)

dept_data = cursor.fetchall()

if dept_data:

    chart_df = pd.DataFrame(
        dept_data,
        columns=[
            "Department",
            "Cases"
        ]
    )

    st.bar_chart(
        chart_df.set_index(
            "Department"
        )
    )

st.divider()

# ==========================
# Appointments
# ==========================

st.subheader("📅 Appointments")

cursor.execute(
    """
    SELECT
        c.patient_name,
        c.department,
        a.appointment_date,
        a.appointment_time,
        a.status
    FROM appointments a
    JOIN cases c
    ON a.case_id = c.id
    ORDER BY a.id DESC
    """
)

appointments = cursor.fetchall()

if appointments:

    appointment_df = pd.DataFrame(
        appointments,
        columns=[
            "Patient",
            "Department",
            "Date",
            "Time",
            "Status"
        ]
    )

    appointment_df.insert(
        0,
        "S.No",
        range(1, len(appointment_df) + 1)
    )

    st.dataframe(
        appointment_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No appointments booked yet."
    )

conn.close()