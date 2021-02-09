"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730410603"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
fortune: int = randint(1, 100)

if fortune <= 25:
    print("Your hard work will soon pay off")
else:
    if fortune <= 50:
        print("A new friend will enter your life")
    else:
        if fortune <= 75:
            print("Be careful to who you listen to today")
        else:
            if fortune <= 100:
                print("A blessing will make it way to you")

print("Now, go spread positive vibes!")