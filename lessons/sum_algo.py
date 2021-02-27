"""Examples of list and loop algortithm."""

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned."""
    # 1. Initialize total and index i to 0
    total: int = 0
    i: int = 0 
    # 2. While i is valid, meaning i < len(xs)
    while i < len(xs): 
        # 2. True) Take xs[i] and add to total
        total  += xs[i] 
        # 2, True) Increase i by 1, moving it to the next index
        i += 1


    # 2. False) Result is stored in total variable
    return total

#Example usage of sum_algo function
odds: list[int] = [1,3,5,7]
odds_sum: int = sum_algo(odds)
print(odds_sum)