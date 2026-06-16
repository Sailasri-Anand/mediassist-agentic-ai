from langgraph.graph import StateGraph, END

from models.state import PatientState

from agents.symptom_agent import symptom_agent
from agents.triage_agent import triage_agent
from agents.routing_agent import routing_agent
from agents.summary_agent import summary_agent

builder = StateGraph(PatientState)

builder.add_node(
    "symptom_analysis",
    symptom_agent
)

builder.add_node(
    "triage",
    triage_agent
)

builder.add_node(
    "routing",
    routing_agent
)

builder.add_node(
    "summary",
    summary_agent
)

builder.set_entry_point(
    "symptom_analysis"
)

builder.add_edge(
    "symptom_analysis",
    "triage"
)

builder.add_edge(
    "triage",
    "routing"
)

builder.add_edge(
    "routing",
    "summary"
)

builder.add_edge(
    "summary",
    END
)

graph = builder.compile()