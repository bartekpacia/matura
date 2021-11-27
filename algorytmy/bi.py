def bsearch(target: int, arr: list[int]) -> int | None:
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]
        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
        else:
            return mid

    return None


def bisect():
    pass
