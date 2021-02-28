"""A choose your own adventure game involving a virtual pet."""

__author__ = "730410603"

from random import randint

def main() -> None:
   """Pet game procedure."""
   player: str = str(input("Name your pet:"))
   greet(player)
   points: int = 0 
   print("Now, choose where you want to go for the day: \'Beach\', \'Park\', or \'Mountain\'. Type \'Exit\' to quit the game.")
   path: str = str(input("Choose where to go:"))
   if path == "Beach":
       Beach(path,player,points)
   else:
       if path == "Park":
           Park(path,player,points) 
       else:
           if path == "Spa":
               Spa(path,player,points)
           else:
               Exit(path,points) 


def greet(player:str) -> None:
    """Game greeting."""
    print(f"In this game, you will be taking care of a virtual pet. You can earn points based on the decisions made regarding your pet. The more points you earn, the stronger the bond between you and your pet. Your pet name is:{player}")


def Beach(path:str, player:str, points:int) -> None:
    """Trip to the beach."""
    while input(f"Do you want to play fench with {player}? yes/no - ") == "yes":
        points += 1
        print(f"You earn {points} points.")
    Exit(path,points)



def Park(path:str, player:str, points:int) -> None:
    """Trip to the park."""
    points = 0 
    while input(f"Do you to rub {player}\'s belly? yes/no - ") == "yes":
        points += 1
        print(f"You earn {points} points.")
    Exit(path,points)


def Spa(path:str, player:str, points:int) -> None:
    """Trip to the spa."""
    while input(f"Do you want to rub {player}\'s fur? yes/no -") == "yes":
        points += 1
        print(f"You earn {points} points.")
    Exit(path,points)


def Exit(path:str,points:int) -> None:
    """Quitting the game."""
    print(f"Thanks for playing the game, you earn {points} points.")

if __name__ == "__main__":  
    main()