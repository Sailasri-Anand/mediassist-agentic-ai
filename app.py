from graph.workflow import graph

from database.db import init_db
from database.save_case import save_case

init_db()

print("\n🏥 MediAssist AI Hospital Assistant")
print("-" * 40)

patient_name = input(
    "\nEnter patient name: "
)

phone = input(
    "Enter phone number: "
)

symptoms = input(
    "Enter symptoms: "
)

result = graph.invoke(
    {
        "patient_name": patient_name,
        "phone": phone,
        "symptoms": symptoms
    }
)

save_case(result)

print("\n" + "=" * 50)

print("\n🔍 AI ASSESSMENT")
print(result["condition"])

print("\n🚨 URGENCY LEVEL")
print(result["urgency"])

print("\n👨‍⚕️ RECOMMENDED DEPARTMENT")
print(result["department"])

print("\n📝 CASE SUMMARY")
print(result["summary"])

print("\n💾 Case successfully saved to hospital database.")

print("\n⚠️ Disclaimer:")
print(
    "This system assists with triage and routing. "
    "It does not provide medical diagnoses."
)

print("\n" + "=" * 50)