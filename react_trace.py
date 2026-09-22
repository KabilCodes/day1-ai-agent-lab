from agent import agent


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)


print("QUESTION:")
print(QUESTION)

print("\n--- THE AGENT'S ACTIONS AND OBSERVATIONS ---")

answer = agent(
    QUESTION,
    max_steps=8
)

print("\nFINAL ANSWER:")
print(answer)