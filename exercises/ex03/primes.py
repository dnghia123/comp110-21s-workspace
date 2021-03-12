"""EX03 - prime functions."""

__author__: str = "730410603"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(110))
    # ex. print(is_prime(5)), print(list_primes(10, 20))
def is_prime(n: int) -> bool:
    """Prime Numbers."""
    if n <= 1:
        return False
    if n % 1 == 0 and n % n == 0:
        return True
    else:
        return False

def list_primes(s: int, t: int) -> list[int]:
    

if __name__ == "__main__":
    main()