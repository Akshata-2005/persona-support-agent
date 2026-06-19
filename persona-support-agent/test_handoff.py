from src.handoff import generate_handoff

summary = generate_handoff(
    "Frustrated User",
    "Unable to reset password",
    ["password_reset.md"]
)

print(summary)