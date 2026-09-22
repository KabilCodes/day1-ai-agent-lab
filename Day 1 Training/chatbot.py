from config import client, MODEL, QUESTIONS, banner

banner("PLAIN LLM CHATBOT")

for i, question in enumerate(QUESTIONS, start=1):

    print(f"Q{i}: {question}")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content.strip()

    print("A:", answer)
    print()