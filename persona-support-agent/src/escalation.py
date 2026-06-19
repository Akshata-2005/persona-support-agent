def should_escalate(user_message, retrieved_docs):

    msg = user_message.lower()

    if any(word in msg for word in [
        "refund",
        "billing dispute",
        "legal",
        "lawsuit",
        "account hacked"
    ]):
        return True

    if len(retrieved_docs) == 0:
        return True

    return False