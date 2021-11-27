def konwertuj(num: int, base: int) -> str | None:
    if num == 0:
        return "0"
    if base < 2:
        return None

    digits: list[str] = []

    while num > 0:
        n_temp = num // base
        digit = num % base
        digits.append(str(digit))
        num = n_temp

    return "".join(digits[::-1])
