def triage_agent(state):

    symptoms = state["symptoms"].lower()

    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "shortness of breath",
        "stroke",
        "unconscious",
        "heart attack",
        "severe bleeding",
        "seizure",
        "heartbeat fast",
        "heart beat fast",
        "rapid heartbeat",
        "palpitations",
        "fainting",
        "passed out",
        "can't breathe",
        "breathing problem"
    ]

    urgency = "Low"

    for keyword in emergency_keywords:

        if keyword in symptoms:

            urgency = "Emergency"
            break

    return {
        "urgency": urgency
    }