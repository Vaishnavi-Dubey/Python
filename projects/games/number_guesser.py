import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than zero nxt time')
        quit()
else:
    print('please type a number next time')
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)

while True:
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    print('after continue')
