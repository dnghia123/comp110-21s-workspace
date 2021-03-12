"""EX03 - palindromify function."""

from typing import ChainMap


__author__: str = "730410603"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("red", True))
    print(palindromify("race", False))
    print(palindromify("nghia", True))
    print(palindromify("nghia", False))


def palindromify(p: str, l: bool) -> str:
    """Converting words to palindrome."""
    i = 0
    cap: list[str] = []
    while i < len(p):
        cap.append(p[i])
        i += 1
    if l is True:
        i = 0 
        length:int = len(cap)
        iteration:int = length - 1
        while i < length + iteration:
            cap.append(cap[(len(cap)-1) - i])
            i += 2 
    if l is False:
        i = 0
        length:int = len(cap)
        iteration: int = length - 2
        while i < length + iteration:
            cap.append(cap[(len(cap)-2) - i])
            i += 2
    word = ""
    for p in cap:
        word += p 
    return word
    
    

if __name__ == "__main__":
    main()