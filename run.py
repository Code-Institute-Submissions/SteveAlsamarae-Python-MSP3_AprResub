import sys


QUESTIONS = [
    "1. Who is the founder of Apple?\n",
    "2. Who is the founder of Microsoft?\n",
    "3. Who is the founder of Google?\n",
    "4. Who is the founder of Facebook?\n",
    "5. Who is the founder of Tesla?\n",
    ]

ANSWERS = [
    "steve jobs",
    "bill gates",
    "larry page",
    "mark zuckerberg",
    "elon musk",
]


def ask_question(question, default_answer):
    try:
        answer = input(question)
    except Exception:
        print("An Error happened during Entering an answer!")
        sys.exit()

    if answer.lower() == default_answer:
        print("Correct!")

        return 1

    print("Incorrect!")

    return 0


def main():

    print("Welcome to my computer quiz!")

    try:
        playing = input("Do you want to play?\n")
    except Exception:
        print("An Error happened during Entering an answer!")
        sys.exit()

    if playing.lower() != "yes":

        sys.exit()

    print("Okay! Let's play :)")

    score = 0

    total_questions = len(QUESTIONS)

    try:
        for i in range(total_questions):
            score += ask_question(QUESTIONS[i], ANSWERS[i])
    except Exception:
        print("An Error happened while checking your answer!")
        sys.exit()

    print("You got " + str(score) + " questions correct!")

    print("You got " + str((score / total_questions) * 100) + "%")


if __name__ == "__main__":
    main()
