def detect_persona(message):

    msg = message.lower()

    if any(word in msg for word in ["api", "error", "authentication", "configuration", "logs"]):
        return "Technical Expert"

    elif any(word in msg for word in ["angry", "frustrated", "nothing works", "urgent", "terrible"]):
        return "Frustrated User"

    else:
        return "Business Executive"