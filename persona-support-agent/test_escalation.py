from src.escalation import should_escalate

print(should_escalate("I want a refund", ["billing_policy.txt"]))
print(should_escalate("How to reset password", ["password_reset.md"]))