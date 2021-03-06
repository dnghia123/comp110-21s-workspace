"""A choose your own adventure game involving a virtual pet."""

__author__ = "730410603"

from random import randint

player: str = " "
points: int = 0
NEUTRAL_PET: str = "\U0001F431" 
HAPPY_PET: str = "\U0001F63A"
EXCITED_PET: str = "\U0001F638"
LOVING_PET: str = "\U0001F63B"


def main() -> None:
    """Pet game procedure."""
    greet()
    print("Choose where to go for the day: \'Beach\', \'Park\', or \'Spa\'. Type \'Exit\' to quit the game.")
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
    global player 
    player = str(input("Name your pet: "))
    print(f"You will be taking care of a virtual pet. Your pet name is: {player}")
    print(f"This is {player}, {NEUTRAL_PET}. The more points you earn, the happier {player} will be")


def Beach(path: str, player: str, points: int) -> None:
    """Trip to the beach."""
    while input(f"Do you want to play fench with {player}? yes/no - ") == "yes":
        points += 10
        print(f"You earn {points} points.")
    treat: str = str(input(f"Give {player} a treat? yes/no - "))
    if treat == "yes":
        points += 25
    else:
        points -= 10
    print(f"You earn {points} points.")
    Exit(path, points)


def Park(path: str, player: str, points: int) -> int:
    """Trip to the park.""" 
    while input(f"Do you wanna look for tennis balls with {player}? yes/no - ") == "yes":
        balls: int = randint(1, 25)
        points += balls
        print(f"Wow, {player} collected {balls} balls")
    Exit(path, points)
    return points


def Spa(path: str, player: str, points: int) -> None:
    """Trip to the spa."""
    while input(f"Do you want to brush {player}\'s fur? yes/no -") == "yes":
        points += 5
        print(f"You earn {points} points.")
    while input(f"Give {player} belly rubs? yes/no - ") == "yes":
        points += 10
        print(f"You earn {points} points.")
    Exit(path, points)


def Exit(path: str, points: int) -> None:
    """Quitting the game."""
    print(f"Thanks for playing the game, you earn {points} points.")
    if points <= 100:
        print(HAPPY_PET)
    else:
        if points <= 150:
            print(EXCITED_PET)
        else:
            if points > 150:
                print(LOVING_PET)
            
            
if __name__ == "__main__":   
    main()