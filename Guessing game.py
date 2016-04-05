range= input('pick a range')
guess= input ('Pick a number within that range')

import random
random_number = (random.randint(1,range))
"""Add a while loop"""
while guess != random_number:
    if guess < random_number:
        print "Guess a little higher"
        guess= input ('Guess again')
    elif guess > random_number:
        print "Guess a little lower"
        guess= input ('Guess again')
    # elif guess == random_number:
print "You guessed right"

"""Get here on time next time. Don't take the bus even if its necessary! TAKE A CAB """
