# 🏥 MediAssist - Agentic AI Hospital Management System

## 📌 Overview

MediAssist is an Agentic AI-powered hospital management system that automates patient triage, emergency detection, department routing, doctor communication, appointment tracking, and administrative monitoring.

The system uses multiple AI agents working together to analyze patient symptoms, determine urgency levels, generate doctor-ready summaries, and route cases to the appropriate medical department.

---

## 🚀 Live Demo


https://mediassist-agentic-ai-hb9nzkb5z5nyi5y4humrca.streamlit.app/Admin

---

## ✨ Features

### 👤 Patient Portal

* Enter patient details and symptoms
* AI symptom analysis
* Automatic urgency detection
* Emergency case identification
* Department recommendation
* AI-generated medical summary

### 🤖 Agentic AI Workflow

* Symptom Analysis Agent
* Triage Agent
* Routing Agent
* Summary Agent

### 👨‍⚕️ Doctor Dashboard

* View assigned patient cases
* Review AI-generated summaries
* Send responses to patients
* Track appointments
* Mark cases as completed

### 👨‍💼 Admin Dashboard

* View all patient cases
* Emergency case monitoring
* Department analytics
* Appointment tracking
* Delete completed or unwanted cases
* Real-time hospital overview

---

## 🧠 Agent Architecture

Patient Symptoms
↓
Symptom Agent
↓
Triage Agent
↓
Routing Agent
↓
Summary Agent
↓
Doctor Dashboard
↓
Admin Dashboard

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python
* SQLite

### AI & Agent Framework

* Google Gemini
* LangChain

### Database

* SQLite3

### Deployment

* GitHub
* Streamlit Cloud

---

## 📂 Project Structure

```text
mediassist-agentic-ai/
│
├── agents/
│   ├── symptom_agent.py
│   ├── triage_agent.py
│   ├── routing_agent.py
│   └── summary_agent.py
│
├── database/
│   ├── db.py
│   ├── save_case.py
│   └── save_appointment.py
│
├── graph/
│   └── workflow.py
│
├── models/
│   └── state.py
│
├── pages/
│   ├── 1_Patient.py
│   ├── 2_Doctor.py
│   └── 3_Admin.py
│
├── home.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔥 Key Highlights

* Agentic AI workflow implementation
* Emergency case prioritization
* Automated hospital triage
* Multi-dashboard architecture
* Real-time patient management
* Cloud deployment ready

---

## 📸 Screenshots

<img width="1491" height="732" alt="image" src="https://github.com/user-attachments/assets/5621edea-a168-48f5-b52a-b74b361ef835" />
<img width="1373" height="756" alt="image" src="https://github.com/user-attachments/assets/8ac1cd69-c108-4993-94ee-baa5d563f3ba" />
<img width="1452" height="710" alt="image" src="https://github.com/user-attachments/assets/0fde770b-f667-4712-9f0f-b0f443205eea" />
<img width="1487" height="736" alt="image" src="https://github.com/user-attachments/assets/a9f57d60-f4a9-4082-ba53-f2a825d536e7" />
<img width="1378" height="593" alt="image" src="https://github.com/user-attachments/assets/1b23e3cc-ddad-4d2a-94d3-408292ee767e" />

---

## 👩‍💻 Author

**Sailasri Anand**
 Cse with Business Analysis , 3rd year student at VIT Chennai.
 
Built as an Agentic AI healthcare automation project using Streamlit, LangChain, Gemini, and SQLite.
