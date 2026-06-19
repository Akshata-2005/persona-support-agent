import streamlit as st

from src.rag_pipeline import search_documents, store_documents
from src.persona_detector import detect_persona
from src.response_generator import generate_response
from src.escalation import should_escalate
from src.handoff import generate_handoff
store_documents()
st.title("Persona-Aware Customer Support Agent")

user_input = st.text_area("Enter your issue")

if st.button("Submit"):

    persona, response = generate_response(user_input)

    results = search_documents(user_input)

    docs_used = []

    if results["metadatas"]:
        docs_used = [
            doc["source"]
            for doc in results["metadatas"][0]
        ]

    escalation = should_escalate(
        user_input,
        docs_used
    )

    st.subheader("Detected Persona")
    st.write(persona)

    st.subheader("Retrieved Sources")
    st.write(docs_used)

    st.subheader("Response")
    st.write(response)

    st.subheader("Escalation Status")
    st.write(escalation)

    if escalation:

        handoff = generate_handoff(
            persona,
            user_input,
            docs_used
        )

        st.subheader("Human Handoff Summary")
        st.json(handoff)