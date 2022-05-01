print("Welcome to my computer quiz!")

playing = input("Do you want to play? \n")


if playing != "yes":
    quit()  # quit() is a python syntax to close the application
print("Okay! lets play")

answer = input("What dose CPU stands for \n")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
