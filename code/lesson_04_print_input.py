"""Build a starter AI prompt from a user's business details and budget."""

# Store input separately so we can greet the user before building the prompt.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

# Convert budget to an integer so it is stored as a number rather than plain text.
budget = int(input("Monthly budget (PKR): "))

print(f"\nWelcome, {name}!")

# Include the budget in the prompt so AI suggestions stay realistic for the business.
prompt = (
    f"Suggest 3 AI solutions for a {business} that struggles with {problem}.\n"
    f"Budget: {budget} PKR per month."
)

print("--- Your AI Prompt ---")
print(prompt)