from collections import Counter

from config import client, MODEL, banner
from cot_compare import COT_PROMPT, QUESTIONS


RUNS = 5
TEMPERATURE = 0.8


def final_answer(text):

    lines = text.splitlines()

    for line in reversed(lines):

        if "final answer" in line.lower():

            if ":" in line:
                return line.split(
                    ":",
                    1
                )[1].strip()

            return line.strip()

    if lines:
        return lines[-1].strip()

    return "(empty)"


def run_many(
    question,
    runs=RUNS,
    temperature=TEMPERATURE
):

    answers = []

    for attempt in range(
        1,
        runs + 1
    ):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": COT_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=temperature
        )

        text = response.choices[0].message.content

        answer = final_answer(text)

        print(
            f"Run {attempt}: {answer}"
        )

        answers.append(answer)

    return answers


if __name__ == "__main__":

    banner("SELF-CONSISTENCY")

    question = QUESTIONS[0]

    print("QUESTION:")
    print(question)

    print(
        f"\nRunning {RUNS} times..."
    )

    answers = run_many(question)

    counter = Counter(answers)

    winner, count = counter.most_common(1)[0]

    print("\nAll answers:")

    for number, answer in enumerate(
        answers,
        start=1
    ):

        print(
            f"{number}. {answer}"
        )

    print(
        f"\nMajority answer "
        f"({count} of {len(answers)} runs):"
    )

    print(winner)