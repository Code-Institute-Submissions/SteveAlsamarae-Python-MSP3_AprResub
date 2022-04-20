"""A web terminal based quiz game built using Python"""

import sys

from utils import colors as c


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
        c.print_error("An Error happened during Entering an answer!")
        sys.exit()

    while not answer:
        try:
            c.print_warning("You did not enter an answer! Try entering an answer!")
            answer: str = input(question)
        except (ValueError, TypeError):
            c.print_error("An Error happened during Entering an answer!")
            sys.exit()

    if answer.lower() == default_answer:
        c.print_result(True, "Correct!")

        return 1

    c.print_result(False, "Incorrect!")
    print(c.cyan("Correct answer is: ") + c.bold_blue(default_answer), "\n")

    return 0


def main() -> None:
    """The main function that runs the quiz."""

    c.print_heading("Welcome to the Quiz!", "You will be asked 5 questions!")

    while True:
        try:
            playing: str = input("Do you want to play?[y/yes]\n")
        except (ValueError, TypeError):
            c.print_error("An Error occurred during confirmation!")

            sys.exit()

        if not playing:
            c.print_warning("You didn't enter an anything!\n")
            continue
        break

    if playing.lower() != "y" and playing.lower() != "yes":
        print(f"{c.cyan('No problem! You can always play later!')}")
        print(f"To play again, click on the {c.bold_underline_blue('RUN PROGRAM')} button.")
        print()
        sys.exit()

    print(c.bold_blue("Let's start the quiz!"), "\n")

    score: int = 0
    total_questions: int = len(QUESTIONS)

    for i in range(total_questions):
        score += ask_question(QUESTIONS[i], ANSWERS[i])

    s_msg = f"You got {score} questions correct out of {total_questions}"
    p_msg = f"Your efficiency is {(score/total_questions * 100)}%"

    c.print_final_result(scores_msg=s_msg, percentage_msg=p_msg, padding=True, pattern_len=60)

    # Exit the program after printing the final result
    sys.exit()


if __name__ == "__main__":
    main()
