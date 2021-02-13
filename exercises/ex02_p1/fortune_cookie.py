"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730410603"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print (fortune_cookie () )
    print("Now, go spread positive vibes!")


def fortune_cookie () -> str: 
    x: int = randint( 1, 100 )
    """Function of fortune cookie."""
    if x <= 25:
        return "Your hard work will soon pay off"
    else:
        if x <= 50:
            return "A new friend will enter your life"
        else:
            if x <= 75:
                return "Be careful to who you listen to today"
    return "A blessing will make it way to you"


# Python Idiom for "starting" the program when run as a module.s
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
