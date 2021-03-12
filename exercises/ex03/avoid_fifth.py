"""EX03 - avoid_fifth function."""

__author__: str = "730410603"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello"))
    print(avoid_fifth("Elephant eat eggplants"))


def avoid_fifth(f: str) -> str:
    """Removing the letter E.""" 
    i: int = 0
    cap: list[str] = []
    while i < len(f):
        cap.append(f[i])
        i += 1
    i = 0 
    while i < len(cap):
        if cap[i] == "E":
            cap.pop(i)
        if cap[i] == "e":
            cap.pop(i)
        i += 1
    word = ""
    for f in cap:
        word += f
    return word
   

if __name__ == "__main__":
    main()