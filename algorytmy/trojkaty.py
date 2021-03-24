def czy_trojkat(a: float, b: float, c: float) -> bool:
    bok_max = max(a, b, c)
    bok_min = min(a, b, c)

    if bok_min + b > bok_max:
        return True

    return False


var = czy_trojkat(3, 4, 6)
print(var)
