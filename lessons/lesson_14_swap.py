"""Swappy"""


def swap(xs: list[int], i: int, j: int) -> None:
    temp: int = xs[i]
    xs[i] = xs[j]
    xs[j] = temp


nums: list[int] = [2, 3, 1, 4]
swap(nums, 2, 1)
swap(nums, 1, 0)
print(nums)