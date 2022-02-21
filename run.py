import sys


def askQuestion(question, defaultAnswer):
    try:
        answer = input(question)
    except Exception:
        print("An Error happened during Entering an answer!")
        sys.exit()

    if answer.lower() == defaultAnswer:
        print("Correct!")

        return 1

    print("Incorrect!")

    return 0


quesitons = [
    "Who is the founder of Apple?\n",
    "Who is the founder of Microsoft?\n",
    "Who is the founder of Google?\n",
    "Who is the founder of Facebook?\n",
    "Who is the founder of Tesla?\n",
    ]

answers = [
    "steve jobs",
    "bill gates",
    "larry page",
    "mark zuckerberg",
    "elon musk",
]


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

    questionsAsked = len(quesitons)

    try:
        for i in range(questionsAsked):
            score += askQuestion(quesitons[i], answers[i])
    except Exception:
        print("An Error happened while checking your answer!")
        sys.exit()

    print("You got " + str(score) + " questions correct!")

    print("You got " + str((score / questionsAsked) * 100) + "%")
main()
    