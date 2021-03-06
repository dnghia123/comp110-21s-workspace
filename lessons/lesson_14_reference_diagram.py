"""Something's up."""


def sum_things_up(xs: list[int]) -> int:
    total: int = 0

    while len(xs) > 0:
        total += xs.pop()

    return total


nums: list[int] = [1, 2, 3]
print(sum_things_up(nums))
print(sum_things_up(nums))