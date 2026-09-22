from config import COURSE_FEES, QUESTIONS, banner

banner("RULE-BASED WORKFLOW")

for i, question in enumerate(QUESTIONS, start=1):

    print(f"Q{i}: {question}")

    q = question.lower()

    if "fee for ai202" in q:
        answer = f"The fee for AI202 is Rs. {COURSE_FEES['AI202']}."

    elif "total fee" in q and "cs101" in q and "ai202" in q:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        scholarship = total * 0.10
        final_fee = total - scholarship

        answer = (
            f"Total fee = Rs. {total}. "
            f"After 10% scholarship = Rs. {final_fee:.0f}."
        )

    elif "ds303" in q and "cs101" in q and "more expensive" in q:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]

        answer = (
            f"Yes. DS303 is more expensive than CS101 "
            f"by Rs. {difference}."
        )

    elif "welcome message" in q:
        answer = (
            "Welcome to the AI program!\n"
            "We are happy to have you join us."
        )

    else:
        answer = "I don't have a rule for this question."

    print("A:", answer)
    print()