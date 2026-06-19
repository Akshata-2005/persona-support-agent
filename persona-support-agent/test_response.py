from src.response_generator import generate_response

persona, response = generate_response(
    "I am unable to reset my password"
)

print("Persona:", persona)
print("\nResponse:")
print(response)