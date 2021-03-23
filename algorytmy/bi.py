from typing import List, Optional


def bsearch(target: int, arr: List[int]) -> Optional[int]:
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]
        if guess < target:
            print(f"{guess=} < {target=}")
            low = mid + 1
        elif guess > target:
            print(f"{guess=} > {target=}")
            high = mid - 1
        else:
            print(f"{guess=} == {target=}")
            return mid

    return None

def bisect():
    pass
