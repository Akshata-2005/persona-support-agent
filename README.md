#Live Demo: https://persona-support-agent-z3ebvv4hja2ffchnkl4qp3.streamlit.app/

# Persona-Aware Customer Support Agent

A customer support chatbot that detects user personas, retrieves relevant support documents using Retrieval-Augmented Generation (RAG), generates persona-specific responses, and escalates complex issues to human agents.

## Features

* Persona Detection
* RAG-based Document Retrieval
* Personalized Responses
* Escalation Detection
* Human Handoff Summary
* Streamlit User Interface

## Technologies Used

* Python
* Streamlit
* ChromaDB
* LangChain Text Splitters
* Google Gemini API

## Project Structure

* data/: Support knowledge base documents
* src/: Core application modules
* app.py: Streamlit interface
* test_*.py: Testing scripts

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
