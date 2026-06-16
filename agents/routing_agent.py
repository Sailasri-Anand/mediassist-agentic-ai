def routing_agent(state):

    symptoms = state["symptoms"].lower()

    department = "General Medicine"

    # Cardiology
    if (
        "chest pain" in symptoms
        or "heart pain" in symptoms
        or "palpitations" in symptoms
        or "heartbeat" in symptoms
        or "heart beat" in symptoms
        or "rapid heartbeat" in symptoms
        or "difficulty breathing" in symptoms
        or "shortness of breath" in symptoms
    ):

        department = "Cardiology"

    # Neurology
    elif (
        "headache" in symptoms
        or "migraine" in symptoms
        or "dizziness" in symptoms
        or "seizure" in symptoms
        or "stroke" in symptoms
    ):

        department = "Neurology"

    # Dermatology
    elif (
        "rash" in symptoms
        or "skin" in symptoms
        or "itching" in symptoms
    ):

        department = "Dermatology"

    # Orthopedics
    elif (
        "bone pain" in symptoms
        or "fracture" in symptoms
        or "joint pain" in symptoms
        or "back pain" in symptoms
    ):

        department = "Orthopedics"

    return {
        "department": department
    }