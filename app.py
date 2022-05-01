print("Welcome to my computer quiz!")

playing = input("Do you want to play? \n")


if playing != "yes":
    quit()  # quit() is a python syntax to close the application
print("Okay! lets play")

score = 0


answer = input("What dose CPU stands for?\n")
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What dose GPU stands for?\n")
if answer.lower() == "graphics processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What dose RAM stands for?\n")
if answer.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("What dose PSU stands for \n")
if answer.lower() == "power supply":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

print(f"The total result is: {score} out of 4")
