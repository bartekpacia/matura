def to_bin(num: int) -> str:
    return bin(num)[2:]


def to_hex(num: int) -> str:
    return hex(num)[2:]


def to_num_system(num: int, base: int) -> str:
    rests: list[str] = []

    while num / base:
        div = num // base
        rest = num % base

        num = div

        if rest == 10:
            rests.append("A")
        elif rest == 11:
            rests.append("B")
        elif rest == 12:
            rests.append("C")
        elif rest == 13:
            rests.append("D")
        elif rest == 14:
            rests.append("E")
        elif rest == 15:
            rests.append("F")
        else:
            rests.append(str(rest))

    rev_rests = rests[::-1]
    return "".join(rev_rests)


def is_palindrome(text: str) -> bool:
    return text == text[::-1]
