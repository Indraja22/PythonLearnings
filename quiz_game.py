print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
reply_yes = "yes"
score = 0

if playing.lower() != reply_yes:
    quit()

print("Okay! Let's Play!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print(f"Your Score Is : {score}")
