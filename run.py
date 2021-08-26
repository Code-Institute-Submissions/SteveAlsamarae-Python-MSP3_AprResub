print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0    


answer = input("Who is the founder of Apple? ")
if answer.lower() == "steve jobs":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Microsoft? ")
if answer.lower() == "bill gates":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Google? ")
if answer.lower() == "larry page":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Facebook? ")
if answer.lower() == "mark zuckerberg":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("Who is the founder of Tesla? ")
if answer.lower() == "elon musk":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")                       