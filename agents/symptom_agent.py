def symptom_agent(state):

    symptoms = state["symptoms"].lower()

    if "chest pain" in symptoms and (
        "breath" in symptoms
        or "breathing" in symptoms
    ):
        assessment = "Possible cardiac emergency"

    elif (
        "fever" in symptoms
        or "cough" in symptoms
    ):
        assessment = "Symptoms suggest possible infection"

    elif (
        "headache" in symptoms
        or "dizziness" in symptoms
    ):
        assessment = "Neurological symptoms require evaluation"

    elif (
        "rash" in symptoms
        or "itching" in symptoms
    ):
        assessment = "Skin symptoms require evaluation"

    else:
        assessment = "Further medical evaluation recommended"

    return {
        "condition": assessment
    }