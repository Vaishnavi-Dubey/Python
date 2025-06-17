print("welcome to my computer quiz")

playing = input("Do you want to play?")

if playing.lower != "yes":
    quit()

print("okay! let's play ;)")
score = 0

answer = input("what does CPU stands for?")
if answer.lower() == "central processing unit":
    print('correct!')
    score = +1
else:
    print("Incorrect!")

answer = input("what does GPU stands for?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score = +1
else:
    print("Incorrect!")

answer = input("what does RAM stands for?")
if answer.lower() == "random access memory":
    print('correct!')
    score = +1
else:
    print("Incorrect!")

print("you got" + str(score) + "questions correct")
print("you got" + str((score / 4) * 100) + "questions correct")
