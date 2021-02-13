"""Tar Heels exercise redux as a structured program."""

__author__ = "730410603"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice)) 


def tar_heels(x: int) -> str:
    """Function of Tar Heels."""
    if x % 2 == 0 and x % 7 == 0:
        return "TAR HEELS"
    else:
        if x % 2 == 0:
            return "TAR"
        else:
            if x % 7 == 0:
                return "HEELS"
    return "CAROLINA"


if __name__ == "__main__":
    main()
