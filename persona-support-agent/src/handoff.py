def generate_handoff(persona, issue, docs_used):

    summary = {
        "persona": persona,
        "issue": issue,
        "documents_used": docs_used,
        "attempted_steps": [],
        "recommendation": "Escalate to human support agent"
    }

    return summary