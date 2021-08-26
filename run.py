print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


answer = input("Who is the founder of Apple?\n")
if answer.lower() == "steve jobs":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Microsoft?\n")
if answer.lower() == "bill gates":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Google?\n")
if answer.lower() == "larry page":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Facebook?\n")
if answer.lower() == "mark zuckerberg":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Tesla?\n")
if answer.lower() == "elon musk":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
