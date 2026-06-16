import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def summary_agent(state):

    prompt = f"""
    Create a short doctor-ready summary.

    Symptoms: {state['symptoms']}
    Urgency: {state['urgency']}
    Department: {state['department']}

    Do not diagnose.
    """

    response = llm.invoke(prompt)

    return {
        "summary": response.content.strip()
    }