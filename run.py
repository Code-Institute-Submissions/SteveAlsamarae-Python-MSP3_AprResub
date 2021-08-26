print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")    


answer = input("Who is the founder of Apple? ")
if answer.lower() == "steve jobs":
    print('Correct!')

else:
    print("Incorrect!")

answer = input("Who is the founder of Microsoft? ")
if answer.lower() == "bill gates":
    print('Correct!')

else:
    print("Incorrect!")

answer = input("Who is the founder of Google? ")
if answer.lower() == "larry page":
    print('Correct!')

else:
    print("Incorrect!")

answer = input("Who is the founder of Facebook? ")
if answer.lower() == "mark zuckerberg":
    print('Correct!')

else:
    print("Incorrect!")

answer = input("Who is the founder of Tesla? ")
if answer.lower() == "elon musk":
    print('Correct!')

else:
    print("Incorrect!")                   