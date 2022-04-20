import sys


QUESTIONS: list[str] = [
    "1. Who is the founder of Apple?\n",
    "2. Who is the founder of Microsoft?\n",
    "3. Who is the founder of Google?\n",
    "4. Who is the founder of Facebook?\n",
    "5. Who is the founder of Tesla?\n",
    ]

ANSWERS: list[str] = [
    "steve jobs",
    "bill gates",
    "larry page",
    "mark zuckerberg",
    "elon musk",
]


def ask_question(question: str, default_answer: str) -> bool:
    """Ask a question and return True if the answer is correct and False if not.

    Args:
        question (str): The question to ask.
        default_answer (str): The answer to the question.

    Returns:
        bool: True if the answer is correct and False if not.
    """

    try:
        answer: str = input(question)
    except (ValueError, TypeError):
        print("An Error happened during Entering an answer!")
        sys.exit()

    while not answer:
        try:
            print("You did not enter an answer! Try entering an answer!")
            answer: str = input(question)
        except (ValueError, TypeError):
            print("An Error happened during Entering an answer!")
            sys.exit()

    if answer.lower() == default_answer:
        print("Correct!")

        return 1

    print("Incorrect!")

    return 0


def main() -> None:
    """The main function that runs the quiz."""

    print("Welcome to my computer quiz!")

    while True:
        try:
            playing: str = input("Do you want to play?[y/yes]\n")
        except (ValueError, TypeError):
            print("An Error occurred during confirmation!")

            sys.exit()

        if not playing:
            print("You didn't enter an anything!\n")
            continue
        break

    if playing.lower() != "y" and playing.lower() != "yes":
        print("No problem! You can always play later!")
        print("Just click on 'RUN PROGRAM' button to play again!")
        print()
        sys.exit()

    print("Let's start the quiz!")

    score: int = 0
    total_questions: int = len(QUESTIONS)

    for i in range(total_questions):
        score += ask_question(QUESTIONS[i], ANSWERS[i])

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / total_questions) * 100) + "%")

    sys.exit()


if __name__ == "__main__":
    main()
