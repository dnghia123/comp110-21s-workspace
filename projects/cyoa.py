"""A choose your own adventure game involving a virtual pet."""

__author__ = "730410603"

from random import randint

def main() -> None:
   """Pet game procedure."""
   player: str = str(input("Enter a name:"))
   greet(player)
   points: int = 0 

def greet(player:str) -> None:
    """Game greeting."""
    print(f"In this game, you will be taking care of a virtual pet. You can earn points based on the decisions made regarding your pet. The more points you earn, the stronger the bond between you and your pet. To begin, name your pet:{player}")


if __name__ == "__main__":  
    main()