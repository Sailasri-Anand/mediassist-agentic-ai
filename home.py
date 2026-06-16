import streamlit as st
from database.db import init_db

init_db()

st.set_page_config(
    page_title="MediAssist AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 MediAssist AI Hospital Management System")

st.markdown("""
### Welcome to MediAssist AI

An Agentic AI-powered Hospital Management System that helps patients, doctors, and administrators collaborate efficiently.

---

### 👤 Patient Portal
- Submit symptoms
- View AI-generated case summary
- View doctor responses
- Book appointments
- Track appointment status

### 👨‍⚕️ Doctor Portal
- Review patient cases
- View AI assessments
- Respond to patients
- Monitor appointment bookings

### 🛠️ Admin Portal
- Monitor all patient cases
- Track emergency cases
- View appointment statistics
- Analyze department workload

---

### 🤖 AI Agents Used

✅ Symptom Analysis Agent

✅ Triage Agent

✅ Department Routing Agent

✅ Case Summary Agent

---

### 🚨 Emergency Detection

The system automatically identifies high-priority symptoms such as:

- Chest Pain
- Difficulty Breathing
- Stroke Symptoms
- Severe Bleeding
- Unconsciousness

and flags them for urgent medical attention.

---

### 📊 Technologies Used

- Python
- Streamlit
- LangGraph
- Gemini AI
- SQLite
- Pandas

---

### Use the sidebar to access:
➡️ Patient Portal

➡️ Doctor Portal

➡️ Admin Portal
""")

st.success("MediAssist AI is ready to use.")