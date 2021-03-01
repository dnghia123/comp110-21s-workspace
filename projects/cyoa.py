"""A choose your own adventure game involving a virtual pet."""

__author__ = "730410603"

from random import randint

player: str = ""
points: int = 0


def main() -> None:
   """Pet game procedure."""
   greet()
   print("Now, choose where you want to go for the day: \'Beach\', \'Park\', or \'Mountain\'. Type \'Exit\' to quit the game.")
   path: str = str(input("Choose where to go:"))
   if path == "Beach":
       Beach(path, player, points)
   else:
       if path == "Park":
           Park(path, player, points)
       else:
           if path == "Spa":
               Spa(path, player, points)
           else:
               Exit(path, points) 


def greet() -> None:
    """Game greeting."""
    player = str(input("Name your pet: "))
    print(f"You will be taking care of a virtual pet. Your pet name is: {player}")


def Beach(path: str, player: str, points: int) -> None:
    """Trip to the beach."""
    while input(f"Do you want to play fench with {player}? yes/no - ") == "yes":
        points += 1
        print(f"You earn {points} points.")
    Exit(path, points)


def Park(path:str, player:str, points:int) -> int:
    """Trip to the park.""" 
    while input(f"Do you wanna look for tennis balls with {player}? yes/no - ") == "yes":
        balls: int = randint(1,25)
        points += balls
        print(f"Wow, {player} collected {balls} balls")
    Exit(path, points)
    return points


def Spa(path: str, player: str, points: int) -> None:
    """Trip to the spa."""
    while input(f"Do you want to rub {player}\'s fur? yes/no -") == "yes":
        points += 1
        print(f"You earn {points} points.")
    Exit(path, points)


def Exit(path: str, points: int) -> None:
    """Quitting the game."""
    print(f"Thanks for playing the game, you earn {points} points.")


if __name__ == "__main__":   
    main()